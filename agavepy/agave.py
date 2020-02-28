from __future__ import absolute_import
import dateutil.parser
import json
import logging
import os
import requests
import sys
import time
import xml.etree.ElementTree as ElementTree

from future import standard_library
standard_library.install_aliases()  # noqa
from urllib.parse import urlsplit  # noqa
from urllib.request import getproxies  # noqa
from urllib.error import HTTPError  # noqa

from agavepy import settings

from agavepy.constants import (CACHES_DOT_DIR, AGPY_FILENAME, CACHE_FILENAME,
                               SESSIONS_FILENAME, TOKEN_SCOPE, TOKEN_TTL,
                               ENV_BASE_URL, ENV_TOKEN, ENV_REFRESH_TOKEN,
                               ENV_USERNAME, ENV_PASSWORD, ENV_API_KEY,
                               ENV_API_SECRET, ENV_TENANT_ID,
                               DEFAULT_TENANT_API_SERVER)

from agavepy.aloe import (LAST_PRE_ALOE_VERSION, EXCEPTION_MODELS)
from agavepy.configgen import (ConfigGen, load_resource)
from agavepy.errors import (AgaveError, AgaveException, __handle_tapis_error,
                            _handle_tapis_error)
from agavepy.interactive import ClientCommands, DeprecatedCommands, TokenCommands
from agavepy.processor import (AgaveProcessor, SwaggerClient, SwaggerClient,
                               SynchronousHttpClient, Operation, Resource)
from agavepy.tenants import id_by_api_server
from agavepy.token import Token
from agavepy.util import AttrDict, json_response, with_refresh

HERE = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(
    os.environ.get('TAPISPY_LOG_LEVEL', logging.WARNING))

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

__all__ = ['Agave']


class Agave(ClientCommands, TokenCommands, DeprecatedCommands):

    can_refresh = True

    PARAMS = [
        # param name, mandatory?, attr_name, default
        ("username", False, "username", None),
        ("password", False, "password", None),
        ("token_username", False, "token_username", None),
        ("jwt", False, "jwt", None),
        ("jwt_header_name", False, "header_name", None),
        ("api_server", False, "api_server", DEFAULT_TENANT_API_SERVER),
        ("tenant_id", False, "tenant_id", None),
        ("expires_in", False, "expires_in", None),
        ("expires_at", False, "expires_at", None),
        ("created_at", False, "created_at", None),
        ("client_name", False, "client_name", None),
        ("api_key", False, "api_key", None),
        ("api_secret", False, "api_secret", None),
        ("token", False, "_token", None),
        ("refresh_token", False, "_refresh_token", None),
        ("use_nonce", False, "use_nonce", False),
        ("resources", False, "resources", None),
        ("verify", False, "verify", True),
        ("token_callback", False, "token_callback", None),
        ("proxies", False, "proxies", getproxies()),
    ]

    def __init__(self, **kwargs):

        self.show_curl = settings.SHOW_CURL

        for param, mandatory, attr, default in self.PARAMS:
            try:
                value = (kwargs[param] if mandatory else kwargs.get(
                    param, default))
            except KeyError:
                raise AgaveError('parameter "{}" is mandatory'.format(param))
            setattr(self, attr, value)

        # Mark the client as unrefreshable if api server and token (but
        # not refresh_token) are provided, as it is considered a 'bare' client
        if self.api_key is None and self.api_secret is None:
            if self.api_server is not None and self._token is not None and self._refresh_token is None:
                setattr(self, 'can_refresh', False)

        if getattr(self, 'resources', None) is None:
            self.resources = load_resource(self.api_server)
        self.resource_exceptions = json.load(
            open(os.path.join(HERE, 'resource_exceptions.json'), 'r'))
        self.host = urlsplit(self.api_server).netloc
        if self.token_callback and not hasattr(self.token_callback,
                                               "__call__"):
            raise AgaveError('token_callback must be callable.')

        # If we are passed a JWT directly, we can bypass OAuth-related tasks
        if self.jwt:
            if not self.header_name:
                raise AgaveError(
                    'The jwt header name is required to use the jwt authenticator.'
                )

        self.token = None
        if (self.api_key is not None and self.api_secret is not None
                and self.jwt is None):
            self.set_client(self.api_key, self.api_secret)
        self.clients_resource = None
        self.all = None
        self.refresh_aris()

        if not hasattr(self, "apps"):
            raise AgaveError(
                "Required parameters for client instantiation missing.")

        logger.debug('Agave: {0}'.format(self))

    def to_dict(self):
        """Return a dictionary representing this client."""
        d = {}
        if hasattr(self, "token") and hasattr(self.token, "token_info"):
            d = {
                "token": self.token.token_info.get("access_token"),
                "refresh_token": self.token.token_info.get("refresh_token"),
                "expires_in": self.token.token_info.get("expires_in"),
                "expires_at": self.token.token_info.get("expires_at"),
                "created_at": self.token.token_info.get("created_at"),
            }
        d.update({
            attr: getattr(self, attr)
            for _, _, attr, _ in self.PARAMS if attr not in [
                "resources",
                "_token",
                "_refresh_token",
                "header_name",
                "jwt",
                "password",
                "token_callback",
            ]
        })
        # If we are writing to the .agave/current file, then
        # modify a few key fields accordingly
        if Agave.agpy_path() == Agave.tapis_current_path():
            d["tenantid"] = d.pop("tenant_id", "")
            d["apisecret"] = d.pop("api_secret", "")
            d["apikey"] = d.pop("api_key", "")
            d["baseurl"] = d.pop("api_server", "")
            d["access_token"] = d.pop("token", "")
        return d

    @classmethod
    def tapis_cache_path(self):
        """Return the path to the credentials cache directory
        """
        agcachedir = os.environ.get(
            "TAPIS_CACHE_DIR",
            os.environ.get("AGAVE_CACHE_DIR",
                           os.path.expanduser(
                               "~/{0}/".format(CACHES_DOT_DIR))))
        if os.path.isdir(agcachedir):
            return agcachedir
        elif not os.path.exists(agcachedir):
            os.makedirs(agcachedir)
            return agcachedir
        else:
            raise ValueError(
                "{0} does not appear to be a directory".format(agcachedir))

    @classmethod
    def tapis_current_path(self):
        """Return path to the current cached credential
        """
        agcachedir = self.tapis_cache_path()
        return os.path.join(agcachedir, CACHE_FILENAME)

    @classmethod
    def tapis_sessions_path(self):
        """Return path to the current sessions cache
        """
        agcachedir = self.tapis_cache_path()
        return os.path.join(agcachedir, SESSIONS_FILENAME)

    @classmethod
    def agpy_path(self):
        """Return path to an .agpy file
        """
        places = [
            self.tapis_current_path(),
            os.path.expanduser("~/{0}".format(AGPY_FILENAME)),
            "/etc/{0}".format(AGPY_FILENAME),
            "/root/{0}".format(AGPY_FILENAME),
            "/{0}".format(AGPY_FILENAME),
        ]
        for place in places:
            if os.path.exists(place):
                return place
        return places[0]

    @classmethod
    def _read_current(cls, agave_kwargs=False):
        with open(Agave.tapis_current_path()) as tcp:
            current = json.loads(tcp.read())
            if agave_kwargs:
                current['tenant_id'] = current.pop('tenantid', '')
                current['api_secret'] = current.pop('apisecret', '')
                current['api_key'] = current.pop('apikey', '')
                current['api_server'] = current.pop('baseurl', '')
                current['token'] = current.pop('access_token', '')
        return current

    @classmethod
    def _read_clients(cls):
        """Read clients from the credential cache file."""
        logger.debug('Agave._read_clients()...')
        with open(Agave.agpy_path()) as agpy:
            clients = json.loads(agpy.read())
        # If we are writing to the .agave/current file, then
        # translate a few key fields accordingly
        if Agave.agpy_path() == Agave.tapis_current_path():
            logger.debug('Using "current" cache format')
            # First, make sure we have a list; The BASH CLI uses a single
            # JSON object but .agpy can store multiple clients in a list
            if not isinstance(clients, list):
                clients = [clients]
            for client in clients:
                # convert CLI keys to agavepy keys:
                for k, v in list(client.items()):
                    if k == "tenantid":
                        client["tenant_id"] = v
                    elif k == "apisecret":
                        client["api_secret"] = v
                    elif k == "apikey":
                        client["api_key"] = v
                    elif k == "baseurl":
                        client["api_server"] = v
                    elif k == "access_token":
                        client["token"] = v
                # add missing attrs:
                if "verify" not in client:
                    # default to verifying SSL:
                    client["verify"] = True
                logger.debug('Found client {0}'.format(client))

        logger.debug('Total clients found: {0}'.format(len(clients)))
        return clients

    @classmethod
    def _read_sessions(cls):
        """Read sessions from the credentials cache."""
        logger.debug('Agave._read_sessions()...')
        try:
            with open(Agave.tapis_sessions_path()) as agsess:
                sessions = json.loads(agsess.read())
        except Exception:
            sessions = {'sessions': {}}
        return sessions

    @classmethod
    def _restore_direct(cls, api_server=None, token=None):
        """Initialize a non-refreshable client from server and token
        """
        if api_server is None:
            api_server = os.environ.get(ENV_BASE_URL, None)
        if token is None:
            token = os.environ.get(ENV_TOKEN, None)
        if api_server is not None and token is not None:
            ag = Agave(api_server=api_server, token=token)
            ag.can_refresh = False
            return ag
        else:
            raise AgaveError(
                'Either api_server or token cannot be resolved from parameters or environment'
            )

    @classmethod
    def _restore_cached(cls, **kwargs):
        """Restore a cached client from a specific attr."""

        try:
            clients = Agave._read_clients()
            # Deal with empty clients file
            if len(clients) == 0:
                logger.error('No clients found in cache.')
                raise AgaveError('No clients found in cache.')
            # If no attribute was passed, restore the first client in the list:
            if len(list(kwargs.items())) == 0:
                return Agave(**clients[0])
            else:
                for k, v in list(kwargs.items()):
                    for client in clients:
                        if client.get(k) == v:
                            return Agave(**client)
            raise AgaveError('Unable to resolve client by keyword')
        except FileNotFoundError:
            raise AgaveError('No cached credentials found')
        except Exception:
            raise

    @classmethod
    def _restore_env(cls):
        # Three types of client can be initialized from env variables
        #
        # 1. refresh is at least able to refresh a token but may also manage clients
        # and issue a new token pair if basic credentials are also provided
        # 2. basic client is only able to interact with clients and issue an initial token
        # 3. bare client is unable to refresh token or manage clients

        clients = {
            'refresh': [(ENV_BASE_URL, 'api_server', True),
                        (ENV_API_KEY, 'api_key', True),
                        (ENV_API_SECRET, 'api_secret', True),
                        (ENV_TOKEN, 'token', True),
                        (ENV_REFRESH_TOKEN, 'refresh_token', True),
                        (ENV_USERNAME, 'username', False),
                        (ENV_PASSWORD, 'password', False)],
            'basic': [(ENV_BASE_URL, 'api_server', True),
                      (ENV_USERNAME, 'username', True),
                      (ENV_PASSWORD, 'password', True),
                      (ENV_API_SECRET, 'api_secret', False),
                      (ENV_API_KEY, 'api_key', False)],
            'bare': [(ENV_BASE_URL, 'api_server', True),
                     (ENV_TOKEN, 'token', True)],
        }

        for kind, envkeys in clients.items():
            try:
                client = {}
                for env, key, req in envkeys:
                    val = os.environ.get(env, None)
                    if val is None and req is True:
                        raise KeyError('{0} must be present')
                    else:
                        client[key] = val
                logger.debug('Client-Type: {}'.format(kind))
                logger.debug('Client: {0}'.format(client))
                return Agave(**client)
            except Exception:
                pass

        logger.warning('restore_env has not returned yet')
        raise AgaveError(
            'One or more missing keys prevent loading a client from the environment'
        )

    @classmethod
    def restore(cls,
                api_key=None,
                client_name=None,
                tenant_id=None,
                token=None,
                api_server=None,
                cache_client=True):
        """Public API to load an Agave client from an external source
        """

        # Attempt bare client first
        try:
            logger.debug('Restore from api_server & token')
            return Agave._restore_direct(api_server=api_server, token=token)
        except AgaveError:
            pass

        # Attempt to load from cache file
        # (works with current, .agpy, and config.json formats)
        try:
            logger.debug('Restore from cached...')
            ag_from_cache = None

            # Resolve from cache by API key
            if api_key:
                logger.debug('By key {0}'.format(api_key))
                ag_from_cache = Agave._restore_cached(api_key=api_key)
            # Resolve from cache by client name
            elif client_name:
                logger.debug('By name {0}'.format(client_name))
                ag_from_cache = Agave._restore_cached(client_name=client_name)
            # Resolve from cache by tenant
            elif tenant_id:
                logger.debug('By tenant {0}'.format(tenant_id))
                ag_from_cache = Agave._restore_cached(tenant_id=tenant_id)
            else:
                # Load up default client
                logger.debug('By default client...')
                ag_from_cache = Agave._restore_cached()

            # Return client, after writing to session file
            if ag_from_cache is not None:
                if cache_client:
                    ag_from_cache._write_client()
                return ag_from_cache

        except FileNotFoundError:
            raise
        except AgaveError:
            pass

        # Attempt to load from environment
        try:
            logger.debug('Restore from env')
            ag = Agave._restore_env()
            if cache_client:
                try:
                    ag._write_client()
                except Exception:
                    raise
            return ag
        except AgaveError:
            pass

        raise AgaveError(
            'Unable to restore a client from parameters, cache, or environment'
        )

    def _write_client(self, permissive=True):
        """Update the credential and sessions cache with the latest values
        """
        # If we are working with an 'current' file, then
        # use the older, less descriptive JSON format
        logger.debug('Agave._write_client()...')
        logger.debug('Target: {0}'.format(Agave.tapis_current_path()))

        if self.can_refresh is False:
            if permissive is False:
                raise NotImplementedError(
                    'Cannot cache credentials if client is not configured for token refresh'
                )
            else:
                return False

        if Agave.agpy_path() == Agave.tapis_current_path():
            logger.debug('writing "current" cache file...')
            new_data = self.to_dict()

            try:
                with open(Agave.agpy_path(), "r") as agpy:
                    old_data = json.loads(agpy.read())
            except Exception:
                old_data = new_data

            # Interesting - we don't seem to carry new_data's time and expiry
            # when writing the cache file. Could that be causing issues w/
            # consumer applications that rely on the cache ttl to implement
            # refresh logic?
            old_data["access_token"] = new_data["access_token"]
            old_data["refresh_token"] = new_data["refresh_token"]

            # Some Tapis client managers drop tenant_id - this fixes that issue
            if getattr(self, 'tenant_id', None) is None:
                self.tenant_id = id_by_api_server(self.api_server)
                new_data['tenantid'] = self.tenant_id

            with open(Agave.agpy_path(), "w") as agpy:
                agpy.write(json.dumps(new_data))
            logger.debug('"current" cache file written')

            try:
                # Write to sessions sidecar
                logger.debug('writing "sessions" cache...')
                sessions = Agave._read_sessions()
                sessions_data = sessions["sessions"]

                tenant_id = new_data["tenantid"]
                username = new_data["username"]

                current_name = new_data.get("client_name", None)
                if current_name is None:
                    current_name = new_data.get("apikey", None)

                if tenant_id not in sessions_data:
                    sessions_data[tenant_id] = {}

                if username not in sessions_data[tenant_id]:
                    sessions_data[tenant_id][username] = {}
                # if current_name not in sessions_data[tenant_id][username]
                # Should probably do an update or merge here
                sessions_data[tenant_id][username][current_name] = new_data
                sessions["sessions"] = sessions_data
                with open(Agave.tapis_sessions_path(), "w") as agsess:
                    agsess.write(json.dumps(sessions))
                logger.debug('"sessions" cache written')

            except Exception as exc:
                # Failure to write sessions file should never cause a failure
                logger.error('failed writing sessions file: {0}'.format(exc))

        else:
            clients = Agave._read_clients()
            new_clients = []
            for client in clients:
                # Update client with the latest representation
                if (client.get("api_key") == self.api_key
                        or client.get("client_name") == self.client_name):
                    new_clients.append(self.to_dict())
                else:
                    # otherwise, write what is already there.
                    new_clients.append(client)
            with open(Agave.agpy_path(), "w") as agpy:
                agpy.write(json.dumps(new_clients))

    def refresh_aris(self):
        logger.debug('Agave.refresh_aris()...')
        self.clients_ari()
        # the resources are defined with a different authenticator in case
        # a jwt is passed in, hence we need to refresh using a different method
        if self.jwt:
            self.jwt_ari()
        elif self.use_nonce:
            self.nonce_ari()
        else:
            self.full_ari()

    def clients_ari(self):
        # If there is enough information to establish HTTP basic auth,
        # then create a 'clients' resource object
        self.clients_resource = self.resource("basic_auth", "host", "username",
                                              "password")

    def full_ari(self):
        # If there is a token, then create a resource object with a
        # bearer token
        self.all = self.resource("token", "host", "_token")

    def nonce_ari(self):
        # if use_nonce is passed in, we use the NonceAuthenticator which does
        # not require any credentials the time of instantiation.
        self.all = self.resource("nonce", "host")

    def jwt_ari(self):
        # If a jwt is passed in, create a resource object with
        # the header_name and jwt token:
        self.all = self.resource("jwt", "host", "header_name", "jwt")

    def resource(self, auth_type, *args):
        logger.debug('Agave.resource({0})...'.format(auth_type))
        args_values = [getattr(self, arg) for arg in args]
        if all(args_values):
            http_client = SynchronousHttpClient(verify=self.verify)
            auth = getattr(http_client, "set_{}".format(auth_type))
            # auth method will be one of: set_basic_auth, set_token,
            # or set_jwt depending on params passed to the constructor.
            auth(*args_values)
            return SwaggerClient(self.resources,
                                 http_client=http_client,
                                 extra_processors=[AgaveProcessor()],
                                 show_curl=self.show_curl)

    def set_client(self, key, secret):
        """
        :type key: str
        :type secret: str
        :rtype: None
        """
        logger.debug('Agave.set_client({0}, {1})...'.format(key, '******'))

        self.api_key = key
        self.api_secret = secret
        self.token = Token(
            self.username,
            self.password,
            self.api_server,
            self.api_key,
            self.api_secret,
            self.verify,
            self,
            self._token,
            self._refresh_token,
            self.token_username,
            self.expires_at,
            self.expires_in,
            self.created_at,
        )
        if self._token:
            logger.debug('self._token exists')
            pass
        else:
            logger.debug('requesting token creation...')
            self.token.create()
        self.refresh_aris()
        logger.debug('set_client() complete')

    def geturl(self, url):
        """Make get request to url using the client access token and retry if token has expired.
        :param url: str
        :return:
        """
        f = requests.get
        return with_refresh(
            self.client,
            f,
            url,
            headers={"Authorization": "Bearer " + self._token},
            verify=self.verify,
            proxies=self.proxies,
        )

    def download_uri(self, uri, local_path):
        """Convenience method to download an agave URL or jobs output URL to an
        absolute `path` on the local file system."""
        if uri.startswith("http") and "jobs" in uri:
            # assume job output uri:
            if "/outputs/listings/" in uri:
                download_url = uri.replace("listings", "media")
            elif "/outputs/media/" in uri:
                download_url = uri
            else:
                raise AgaveError("Unsupported jobs URI.")
        elif "agave://" in uri:
            # assume it is an agave uri
            system_id, path = uri.split("agave://")[1].split("/", 1)
            download_url = "{}/files/v2/media/system/{}/{}".format(
                self.api_server, system_id, path)
        else:
            raise AgaveError("Unsupported URI.")
        f = requests.get
        with open(local_path, "wb") as loc:
            rsp = with_refresh(
                self.client,
                f,
                download_url,
                headers={"Authorization": "Bearer " + self._token},
                verify=self.verify,
                proxies=self.proxies,
            )
            rsp.raise_for_status()
            if type(rsp) == dict:
                raise AgaveError(
                    "Error downloading file at URI: {}, Response: {}".format(
                        uri, rsp))
            for block in rsp.iter_content(1024):
                if not block:
                    break
                loc.write(block)

    def __getattr__(self, key):
        return Resource(key, client=self)

    def __dir__(self):
        base = []
        if hasattr(self, "clients_resource") and hasattr(
                self.clients_resource, "resources"):
            base.extend(list(self.clients_resource.resources.keys()))
        if self.all is not None:
            base.extend(list(self.all.resources.keys()))
        return list(set(base))
