from __future__ import print_function
from builtins import input

import xml.etree.ElementTree as ElementTree
from functools import wraps

from future import standard_library
standard_library.install_aliases()

#import urllib.parse
import urllib.request, urllib.parse, urllib.error
import os
import shelve
from contextlib import closing
import json
import time

import jinja2
import dateutil.parser
import requests

from agavepy.tenants import tenant_list
from agavepy.clients import clients_create, clients_list
from agavepy.tokens import token_create
from agavepy.utils import save_config

import sys
sys.path.insert(0, os.path.dirname(__file__))

from .swaggerpy.client import SwaggerClient
from .swaggerpy.http_client import SynchronousHttpClient
from .swaggerpy.processors import SwaggerProcessor


HERE = os.path.dirname(os.path.abspath(__file__))


def json_response(f):
    @wraps(f)
    def _f(*args, **kwargs):
        resp = f(*args, **kwargs)
        resp.raise_for_status()
        return resp.json()
    return _f


def save(client, key, secret):
    """

    :type client: str
    :type key: str
    :type secret: str
    :rtype: None
    """
    with closing(shelve.open(os.path.expanduser('~/.agavepy'))) as agavepyrc:
        agavepyrc[str(client)] = (key, secret)


def recover(name):
    """Try to recover api keys for client ``name``.

    :type name: str
    :rtype: (str, str)
    """
    with closing(shelve.open(os.path.expanduser('~/.agavepy'))) as agavepyrc:
        return agavepyrc[str(name)]


def load_resource(api_server):
    """Load a default resource file.

    :type api_server: str
    :rtype: dict
    """
    conf = ConfigGen('resources.json.j2')
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(HERE),
                             trim_blocks=True, lstrip_blocks=True)
    rsrcs = json.loads(conf.compile(
        {'api_server_base': urllib.parse.urlparse(api_server).netloc}, env))
    return rsrcs

def with_refresh(client, f, *args, **kwargs):
    """Call function ``f`` and refresh token if needed."""
    try:
        return f(*args, **kwargs)
    except requests.exceptions.HTTPError as exc:
        try:
            # Old versions of APIM return errors in XML:
            code = ElementTree.fromstring(exc.response.text)[0].text
        except Exception:
            # Any error here means the response was not XML.
            try:
                # Try to see if it's a json response,
                exc_json = exc.response.json()
                # if so, check if it is an expired token error (new versions of APIM return JSON errors):
                if 'Invalid Credentials' in exc_json.get('fault').get('message'):
                    client.token.refresh()
                    return f(*args, **kwargs)
                #  otherwise, return the JSON
                return exc.response
            except Exception:
                # Re-raise it, as it's not an expired token
                raise exc
        # only catch 'token expired' exception
        # other codes may mean a different error
        if code not in ['900903', '900904']:
            raise
        client.token.refresh()
        return f(*args, **kwargs)


class ConfigGen(object):
    def __init__(self, template_str):
        self.template_str = template_str

    def compile(self, configs, env):
        template = env.get_template(self.template_str)
        return template.render(configs)


class Token(object):

    def __init__(self,
                 username, password,
                 api_server, api_key, api_secret, verify,
                 parent, _token=None, _refresh_token=None, token_username=None,
                 expires_at=None, expires_in=None, created_at=None):
        self.username = username
        self.password = password
        self.api_server = api_server
        self.api_key = api_key
        self.api_secret = api_secret
        self.token_username = token_username
        # Agave object that created this token
        self.parent = parent
        self.verify = verify
        if _token and _refresh_token:
            self.token_info = {'access_token': _token,
                               'refresh_token': _refresh_token}
            self.token_info['expires_at'] = expires_at
            self.token_info['expires_in'] = expires_in
            self.token_info['created_at'] = created_at
            self.parent._token = _token

        self.token_url = urllib.parse.urljoin(str(self.api_server), 'token')

    def _token(self, data):
        auth = requests.auth.HTTPBasicAuth(self.api_key, self.api_secret)
        resp = requests.post(self.token_url, data=data, auth=auth,
                             verify=self.verify, proxies=self.parent.proxies)
        resp.raise_for_status()
        self.token_info = resp.json()
        try:
            expires_in = int(self.token_info.get('expires_in'))
        except ValueError:
            expires_in = 3600
        created_at = int(time.time())
        self.token_info['created_at'] = created_at
        self.token_info['expiration'] = created_at + expires_in
        self.token_info['expires_at'] = time.ctime(created_at + expires_in)
        token = self.token_info['access_token']
        # Update parent with new token data
        self.parent._token = token
        self.parent.refresh_token = self.token_info['refresh_token']
        self.parent.created_at = self.token_info['created_at']
        self.parent.expiration = self.token_info['expiration']
        self.parent.expires_at = self.token_info['expires_at']
        # try to persist the token data
        try:
            self.parent._write_client()
        except Exception as e:
            # writing the cache file cannot block use.
            pass
        if self.parent.token_callback:
            self.parent.token_callback(**self.token_info)
        self.parent.refresh_aris()
        return token

    def create(self):
        data = {'grant_type': 'password',
                'username': self.username,
                'password': self.password,
                'scope': 'PRODUCTION'}
        if self.token_username:
            data['grant_type'] = 'admin_password'
            data['token_username'] = self.token_username
        return self._token(data)

    def refresh(self):
        data = {'grant_type': 'refresh_token',
                'scope': 'PRODUCTION',
                'refresh_token': self.token_info['refresh_token']}
        return self._token(data)


class AgaveError(Exception):
    pass


class Agave(object):

    PARAMS = [
        # param name, mandatory?, attr_name, default
        ('username', False, 'username', None),
        ('password', False, 'password', None),
        ('token_username', False, 'token_username', None),
        ('jwt', False, 'jwt', None),
        ('jwt_header_name', False, 'header_name', None),
        ('api_server', True, 'api_server', None),
        ('tenant_id', False, 'tenant_id', None),
        ('expires_in', False, 'expires_in', None),
        ('expires_at', False, 'expires_at', None),
        ('created_at', False, 'created_at', None),
        ('client_name', False, 'client_name', None),
        ('api_key', False, 'api_key', None),
        ('api_secret', False, 'api_secret', None),
        ('token', False, '_token', None),
        ('refresh_token', False, '_refresh_token', None),
        ('use_nonce', False, 'use_nonce', False),
        ('resources', False, 'resources', None),
        ('verify', False, 'verify', True),
        ('token_callback', False, 'token_callback', None),
        ('proxies', False, 'proxies', urllib.request.getproxies())
    ]

    def __init__(self, **kwargs):
        
        for param, mandatory, attr, default in self.PARAMS:
            try:
                value = (kwargs[param] if mandatory 
                        else kwargs.get(param, default))
            except KeyError:
                pass

            setattr(self, attr, value)

        # The following sectionsets tenant ID (tenant_id) and tenant url 
        # (api_server).
        # Neither tenant ID nor tenant url are set.
        if self.tenant_id is None and self.api_server is None:
            tenants = self.list_tenants(tenantsurl="https://api.tacc.utexas.edu/tenants")
            value = input("\nPlease specify the ID for the tenant you wish to interact with: ")
            self.tenant_id  = tenants[value]["id"]
            tenant_url = tenants[value]["url"]
            if tenant_url[-1] == '/':
                tenant_url = tenant_url[:-1]
            self.api_server = tenant_url
        # Tenant ID was not set.
        elif self.tenant_id is None and self.api_server is not None:
            tenants = tenant_list(tenantsurl="https://api.tacc.utexas.edu/tenants")

            for _, tenant in tenants.items():
                if self.api_server in tenant["url"]:
                    self.tenant_id = tenant["id"]
        # Tenant url was not set.
        elif self.api_server is None and self.tenant_id is not None:
            tenants = tenant_list(tenantsurl="https://api.tacc.utexas.edu/tenants")

            tenant_url = tenants[self.tenant_id]["url"]
            if tenant_url[-1] == '/':
                tenant_url = tenant_url[:-1]
            self.api_server = tenant_url
    

        if self.resources is None:
            self.resources = load_resource(self.api_server)
        self.host = urllib.parse.urlsplit(self.api_server).netloc
        if self.token_callback and not hasattr(self.token_callback, '__call__'):
            raise AgaveError('token_callback must be callable.')
        # If we are passed a JWT directly, we can bypass all OAuth-related tasks
        if self.jwt:
            if not self.header_name:
                raise AgaveError("The jwt header name is required to use the jwt authenticator.")
        # If we are given a client name and no keys, then try to retrieve
        # them from a persistent file.
        if (self.client_name is not None
                and self.api_key is None and self.api_secret is None):
            self.api_key, self.api_secret = recover(self.client_name)
        self.token = None
        if self.api_key is not None and self.api_secret is not None and self.jwt is None:
            self.set_client(self.api_key, self.api_secret)
        self.clients_resource = None
        self.all = None
        self.refresh_aris()
        if not hasattr(self, 'apps'):
            raise AgaveError('Required parameters for client instantiation missing.')

    def to_dict(self):
        """Return a dictionary representing this client."""
        d = {}
        if hasattr(self, 'token') and hasattr(self.token, 'token_info'):
            d = {'token': self.token.token_info.get('access_token'),
                 'refresh_token': self.token.token_info.get('refresh_token'),
                 'expires_in': self.token.token_info.get('expires_in'),
                 'expires_at': self.token.token_info.get('expires_at'),
                 'created_at': self.token.token_info.get('created_at'),
                 }
        d.update({attr: getattr(self, attr) for _, _, attr, _ in self.PARAMS \
                         if not attr in ['resources', '_token', '_refresh_token', 'header_name', 'jwt', 'password', 'token_callback']})
        # if we are writing to the .agave/current file, modify the fields accordingly
        if Agave.agpy_path() == Agave.agavecurrent_path():
            d['tenantid'] = d.pop('tenant_id', '')
            d['apisecret'] = d.pop('api_secret', '')
            d['apikey'] = d.pop('api_key', '')
            d['baseurl'] = d.pop('api_server', '')
            d['access_token'] = d.pop('token', '')
        return d

    @classmethod
    def agavecurrent_path(self):
        """Return path to .agave/current file allowing for AGAVE_CACHEDIR"""
        agcachedir = os.environ.get('AGAVE_CACHE_DIR', None)
        if agcachedir is not None:
            if os.path.isdir(agcachedir):
                return os.path.join(agcachedir, 'current')
        else:
            return os.path.expanduser('~/.agave/current')

    @classmethod
    def agpy_path(self):
        """Return path to .agpy file"""
        places = [self.agavecurrent_path(),
                  os.path.expanduser('~/.agpy'),
                  '/etc/.agpy',
                  '/root/.agpy',
                  '/.agpy']
        for place in places:
            if os.path.exists(place):
                return place

    @classmethod
    def _read_clients(cls):
        """Read clients from the .agpy file."""
        with open(Agave.agpy_path()) as agpy:
            clients = json.loads(agpy.read())
        # if we are reading an '.agave/current' file, we need to do some translation
        if Agave.agpy_path() == Agave.agavecurrent_path():
            # first, make sure we have a list; in past versions of the CLI, the current file was a
            # single JSON object
            if not isinstance(clients, list):
                clients = [clients]
            for client in clients:
                # convert CLI keys to agavepy keys:
                for k, v in list(client.items()):
                    if k == 'tenantid':
                        client['tenant_id'] = v
                    elif k == 'apisecret':
                        client['api_secret'] = v
                    elif k == 'apikey':
                        client['api_key'] = v
                    elif k == 'baseurl':
                        client['api_server'] = v
                    elif k == 'access_token':
                        client['token'] = v
                # add missing attrs:
                if 'verify' not in client:
                    # default to verifying SSL:
                    client['verify'] = True
        return clients

    @classmethod
    def _restore_client(cls, **kwargs):
        """Restore a client from a specific attr."""
        clients = Agave._read_clients()
        if len(clients) == 0:
            raise AgaveError("No clients found.")
        # if no attribute was passed, we'll just restore the first client in the list:
        if len(list(kwargs.items())) == 0:
            return Agave(**clients[0])
        for k, v in list(kwargs.items()):
            for client in clients:
                if client.get(k) == v:
                    return Agave(**client)
        raise AgaveError("No matching client found.")

    @classmethod
    def restore(cls, api_key=None, client_name=None, tenant_id=None):
        """Public API to restore an agave client from a file."""
        if api_key:
            return Agave._restore_client(api_key=api_key)
        elif client_name:
            return Agave._restore_client(client_name=client_name)
        elif tenant_id:
            return Agave._restore_client(tenant_id=tenant_id)
        else:
            return Agave._restore_client()

    def _write_client(self):
        """Update the .agpy file with the description of a client."""
        # if we are reading the '.agave/current' file, we need to use that format and simply update
        # a few fields
        if Agave.agpy_path() == Agave.agavecurrent_path():
            with open(Agave.agpy_path(), 'r') as agpy:
                old_data = json.loads(agpy.read())
            new_data = self.to_dict()
            old_data['access_token'] = new_data['access_token']
            old_data['refresh_token'] = new_data['refresh_token']
            with open(Agave.agpy_path(), 'w') as agpy:
                agpy.write(json.dumps(new_data))

        else:
            clients = Agave._read_clients()
            new_clients = []
            for client in clients:
                # if this is the current client, update with the latest representation
                if client.get('api_key') == self.api_key or client.get('client_name') == self.client_name:
                    new_clients.append(self.to_dict())
                else:
                    # otherwise, write what is already there.
                    new_clients.append(client)
            with open(Agave.agpy_path(), 'w') as agpy:
                agpy.write(json.dumps(new_clients))

    def refresh_aris(self):
        self.clients_ari()
        # the resources are defined with a different authenticator in case a jwt is passed in, hence
        # we need to refresh using a different method
        if self.jwt:
            self.jwt_ari()
        elif self.use_nonce:
            self.nonce_ari()
        else:
            self.full_ari()

    def clients_ari(self):
        # If there is enough information to establish HTTP basic auth,
        # then create a 'clients' resource object
        self.clients_resource = self.resource(
            'basic_auth', 'host', 'username', 'password')

    def full_ari(self):
        # If there is a token, then create a resource object with a
        # bearer token
        self.all = self.resource(
            'token', 'host', '_token')

    def nonce_ari(self):
        # if use_nonce is passed in, we use the NonceAuthenticator which does not require any credentials at
        # the time of instantiation.
        self.all = self.resource('nonce', 'host')

    def jwt_ari(self):
        # If a jwt is passed in, create a resource object with the header_name and jwt token:
        self.all = self.resource('jwt', 'host', 'header_name', 'jwt')

    def resource(self, auth_type, *args):
        args_values = [getattr(self, arg) for arg in args]
        if all(args_values):
            http_client = SynchronousHttpClient(verify=self.verify)
            auth = getattr(http_client, 'set_{}'.format(auth_type))
            # auth method will be one of: set_basic_auth, set_token, set_jwt depending on params passed to
            # constructor.
            auth(*args_values)
            return SwaggerClient(
                self.resources, http_client=http_client,
                extra_processors=[AgaveProcessor()])

    def set_client(self, key, secret):
        """

        :type key: str
        :type secret: str
        :rtype: None
        """
        self.api_key = key
        self.api_secret = secret
        self.token = Token(
            self.username, self.password,
            self.api_server, self.api_key, self.api_secret,
            self.verify,
            self,
            self._token,
            self._refresh_token,
            self.token_username,
            self.expires_at,
            self.expires_in,
            self.created_at)
        if self._token:
            pass
        else:
            self.token.create()
        self.refresh_aris()

    def geturl(self, url):
        """Make get request to url using the client access token and retry if token has expired.
        :param url: str
        :return:
        """
        f = requests.get
        return with_refresh(self.client, f, url,
                            headers={'Authorization': 'Bearer ' + self._token},
                            verify=self.verify,
                            proxies=self.proxies)

    def download_uri(self, uri, local_path):
        """Convenience method to download an agave URL or jobs output URL to an
        absolute `path` on the local file system."""
        if uri.startswith('http') and 'jobs' in uri:
            # assume job output uri:
            if '/outputs/listings/' in uri:
                download_url = uri.replace('listings', 'media')
            elif '/outputs/media/' in uri:
                download_url = uri
            else:
                raise AgaveError("Unsupported jobs URI.")
        elif 'agave://' in uri:
            # assume it is an agave uri
            system_id, path = uri.split('agave://')[1].split('/', 1)
            download_url = '{}/files/v2/media/system/{}/{}'.format(self.api_server, system_id, path)
        else:
            raise AgaveError("Unsupported URI.")
        f = requests.get
        with open(local_path, 'wb') as loc:
            rsp = with_refresh(self.client, f, download_url,
                               headers={'Authorization': 'Bearer ' + self.token.token_info['access_token']},
                               verify=self.verify,
                               proxies=self.proxies)
            rsp.raise_for_status()
            if type(rsp) == dict:
                raise AgaveError("Error downloading file at URI: {}, Response: {}".format(uri, rsp))
            for block in rsp.iter_content(1024):
                if not block:
                    break
                loc.write(block)


    def __getattr__(self, key):
        return Resource(key, client=self)

    def __dir__(self):
        base = []
        if hasattr(self, 'clients_resource') and hasattr(self.clients_resource, 'resources'):
            base.extend(list(self.clients_resource.resources.keys()))
        if self.all is not None:
            base.extend(list(self.all.resources.keys()))
        return list(set(base))


    def save_configs(self, cache_dir=None):
        """ Save configs

        Save configuration to AGAVE_CACHE_DIR. This will update 
        AGAVE_CACHE_DIR/current and AGAVE_CACHE_DIR/config.json.
        
        PARAMETERS
        ----------
        cache_dir: string (default: None)
            If no cache_dir is passed it will default to ~/.agave.
        """
        current_context = {
            "tenantid": self.tenant_id,
            "baseurl": self.api_server,
            "devurl": "",
            "apisecret": self.api_secret,
            "apikey": self.api_key,
            "username": self.username,
            "access_token": self.token,
            "refresh_token": self.refresh_token,
            "created_at": self.created_at,
            "expires_in": self.expires_in,
            "expires_at": self.expires_at,
        }

        # Convert None values to empty strings.
        for k, v in current_context.items():
            if v is None or isinstance(v, Resource):
                current_context[k] = ""

        if cache_dir is None:
            cache_dir = os.path.expanduser("~/.agave")
        save_config(cache_dir, current_context)


    def list_tenants(self, tenantsurl="https://api.tacc.utexas.edu/tenants"):
        """ List Agave tenants

        PARAMETERS
        ----------
        tenantsurl: string (default: "https://api.tacc.utexas.edu/tenants")
            Endpoint with Agave tenant information.
        """
        tenants = tenant_list(tenantsurl)
        print("{0:<20} {1:<40} {2:<50}".format("ID", "NAME", "URL"))
        for _, tenant in tenants.items():
            print("{0:<20} {1:<40} {2:<50}".format(
                    tenant["id"], tenant["name"], tenant["url"]))

        return tenants


    def clients_create(self, client_name, description):
        """ Create an Agave Oauth client

        Save the api key and secret upon a successfull reuest to Agave.

        PARAMETERS
        ----------
        client_name: string
            Name of the oauth client to be created.
        description: string
            Description of the client to be created.
        """
        # Set tenant url.
        tenant_url = self.api_server
        
        # Set username.
        if self.username == "" or self.username is None:
            self.username = input("API username: ")

        self.api_key, self.api_secret = clients_create(
            self.username, client_name, description, tenant_url)


    def clients_list(self):
        """ List all Agave oauth clients
        """
        # Set username.
        if self.username == "" or self.username is None:
            self.username = input("API username: ")

        # Set tenant url.
        tenant_url = self.api_server

        clients_list(self.username, tenant_url)


    def get_access_token(self):
        """ Generate an access token
        """
        # Check that a client for this session has been created by checking api
        # key and secret.
        if (self.api_key == "" or self.api_key is None or 
                self.api_secret == "" or self.api_secret is None):
            print("Please create a client first. See \"clients_create(client_name, description)\"\n")
            return

        # Set tenant url.
        tenant_url = self.api_server

        # Set username.
        if self.username == "" or self.username is None:
            self.username = input("API username: ")

        # Create access token.
        token_data = token_create(self.username, self.api_key, self.api_secret, tenant_url)

        # Update client.
        self.token         = token_data.get("access_token")
        self.refresh_token = token_data.get("refresh_token")
        self.expires_in    = token_data.get("expires_in")
        self.created_at    = token_data.get("created_at")
        self.expires_at    = token_data.get("expires_at")






class Resource(object):

    def __init__(self, resource, client):
        self.resource = resource
        self.client = client

    def __getattr__(self, attr):
        return Operation(self.resource, attr, client=self.client)

    def __dir__(self):
        if hasattr(self, 'clients_resource') and hasattr(self.clients_resource, 'resources'):
            clients = self.client.clients_resource.resources
            base = list(clients[self.resource].operations.keys())
        else:
            base = []
        if self.client.all is not None:
            base.extend(
                list(self.client.all.resources[self.resource].operations.keys()))
        return base


class AgaveException(Exception):
    pass


class Operation(object):

    PRIMITIVE_TYPES = ['array', 'string', 'integer', 'int', 'boolean', 'dict']

    def __init__(self, resource, operation, client):
        self.resource = resource
        self.operation = operation
        self.client = client

        self.models = self.get_models()
        self.return_type = self.get_return_type()

    def get_base(self):
        """Get the base ari for this resource."""

        return (self.client.clients_resource if self.resource == 'clients'
                else self.client.all)

    def get_operation(self):
        base = self.get_base()
        return getattr(getattr(base, self.resource), self.operation)

    def get_models(self):
        """Get JSON with all the models declarations."""

        base = self.get_base()
        return getattr(base, self.resource).json['api_declaration']['models']

    def get_return_type(self):
        """Get JSON with the return type for this operation."""

        return self.get_operation().json

    def __call__(self, *args, **kwargs):

        def operation():
            f = self.get_operation()
            response = f(*args, **kwargs)
            response.raise_for_status()
            return response

        kwargs['proxies'] = self.client.proxies
        resp = with_refresh(self.client, operation)
        if resp.ok:
            # if response is 204 (no content) return none directly
            if resp.status_code == 204 and not resp.content:
                return resp
            # if response is raw file, return it directly
            if (self.resource == 'files' and
                    (self.operation == 'download'
                     or self.operation == 'downloadFromDefaultSystem')):
                return resp
            # if response is a result, return it directly as well:
            if (self.resource == 'actors' and self.operation == 'getOneExecutionResult'):
                return resp
            processed = self.post_process(resp.json(), self.return_type)
            result = processed['result'] if 'result' in processed else None
            # if operation is clients.create, save name
            if self.resource == 'clients' and self.operation == 'create':
                save(result['name'],
                     result['consumerKey'],
                     result['consumerSecret'])
                self.client.set_client(result['consumerKey'],
                                       result['consumerSecret'])
            return result
        else:
            # if the response is not 2xx return the unprocessed json rather
            # than raising an exception, since the return json contains
            # the error message
            raise AgaveException(resp.json())

    def post_process(self, obj, return_type):
        if return_type is None:
            return self.process_untyped(obj)
        type_name = return_type['type'].lower()
        if type_name in self.PRIMITIVE_TYPES:
            f = getattr(self, 'process_{}'.format(type_name))
            return f(obj, return_type)
        return self.process_model(obj, return_type)

    def process_untyped(self, obj):
        return obj

    def process_dict(self, obj, return_type):
        return obj

    def process_array(self, obj, return_type):
        items = return_type['items']
        items_type = items.get('type', items.get('$ref'))
        return [self.post_process(elem, {'type': items_type})
                for elem in obj]

    def process_string(self, obj, return_type):
        if obj is None:
            # why is agave returning null for a string type?
            return obj
        if return_type.get('format') == 'date-time':
            return dateutil.parser.parse(obj)
        return obj

    def process_integer(self, obj, return_type):
        return obj

    process_int = process_integer

    def process_boolean(self, obj, return_type):
        return obj

    def process_model(self, obj, return_type):
        model_name = return_type['type']
        model_spec = self.models[model_name]['properties']
        return AttrDict({k: self.post_process(obj[k], model_spec.get(k))
                         for k in obj})


class AttrDict(dict):

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


class AgaveProcessor(SwaggerProcessor):

    def process_property(self, resources, resource, model, prop, context):
        if prop.get('format', None) == 'date-time':
            pass

    def process_model(self, resources, resource, model, context):
        pass
