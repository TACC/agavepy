import xml.etree.ElementTree as ElementTree
from functools import wraps
import urlparse
import os
import shelve
from contextlib import closing
import json

import dateutil.parser
import requests

import sys
sys.path.insert(0, os.path.dirname(__file__))

from swaggerpy.client import SwaggerClient
from swaggerpy.http_client import SynchronousHttpClient
from swaggerpy.processors import SwaggerProcessor


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
        agavepyrc[client] = (key, secret)


def recover(name):
    """Try to recover api keys for client ``name``.

    :type name: str
    :rtype: (str, str)
    """
    with closing(shelve.open(os.path.expanduser('~/.agavepy'))) as agavepyrc:
        return agavepyrc[name]


def load_resource(api_server):
    """Load a default resource file.

    :type api_server: str
    :rtype: dict
    """
    rsrcs = json.load(
        open(os.path.join(os.path.dirname(__file__), 'resources.json')))
    return rsrcs


class Token(object):

    def __init__(self,
                 username, password,
                 api_server, api_key, api_secret, verify,
                 parent):
        self.username = username
        self.password = password
        self.api_server = api_server
        self.api_key = api_key
        self.api_secret = api_secret
        # Agave object that created this token
        self.parent = parent
        self.verify = verify

        self.token_url = urlparse.urljoin(self.api_server, 'token')

    def _token(self, data):
        auth = requests.auth.HTTPBasicAuth(self.api_key, self.api_secret)
        resp = requests.post(self.token_url, data=data, auth=auth,
                             verify=self.verify)
        resp.raise_for_status()
        self.token_info = resp.json()
        token = self.token_info['access_token']
        # Notify parent that a token was created
        self.parent._token = token
        self.parent.refresh_aris()
        return token

    def create(self):
        data = {'grant_type': 'password',
                'username': self.username,
                'password': self.password,
                'scope': 'PRODUCTION'}
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
        ('api_server', True, 'api_server', None),
        ('client_name', False, 'client_name', None),
        ('api_key', False, 'api_key', None),
        ('api_secret', False, 'api_secret', None),
        ('token', False, '_token', None),
        ('resources', False, 'resources', None),
        ('verify', False, 'verify', True)
    ]

    def __init__(self, **kwargs):
        for param, mandatory, attr, default in self.PARAMS:
            try:
                value = (kwargs[param] if mandatory
                         else kwargs.get(param, default))
            except KeyError:
                raise AgaveError(
                    'parameter "{}" is mandatory'.format(param))
            setattr(self, attr, value)

        if self.resources is None:
            self.resources = load_resource(self.api_server)
        self.host = urlparse.urlsplit(self.api_server).netloc
        # If we are given a client name and no keys, then try to retrieve
        # them from a persistent file.
        if (self.client_name is not None
                and self.api_key is None and self.api_secret is None):
            self.api_key, self.api_secret = recover(self.client_name)
        self.token = None
        if self.api_key is not None and self.api_secret is not None:
            self.set_client(self.api_key, self.api_secret)
        self.clients_resource = None
        self.all = None
        self.refresh_aris()

    def refresh_aris(self):
        self.clients_ari()
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

    def resource(self, auth_type, *args):
        args_values = [getattr(self, arg) for arg in args]
        if all(args_values):
            http_client = SynchronousHttpClient(verify=self.verify)
            auth = getattr(http_client, 'set_{}'.format(auth_type))
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
            self)
        self.token.create()
        self.refresh_aris()

    def __getattr__(self, key):
        return Resource(key, client=self)

    def __dir__(self):
        base = self.clients_resource.resources.keys()
        if self.all is not None:
            base.extend(self.all.resources.keys())
        return list(set(base))


class Resource(object):

    def __init__(self, resource, client):
        self.resource = resource
        self.client = client

    def __getattr__(self, attr):
        return Operation(self.resource, attr, client=self.client)

    def __dir__(self):
        base = self.client.clients_resource.resources[self.resource].operations.keys()
        if self.client.all is not None:
            base.extend(
                self.client.all.resources[self.resource].operations.keys())
        return base


class Operation(object):

    PRIMITIVE_TYPES = ['array', 'string', 'integer', 'int', 'boolean']

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

    def _with_refresh(self, f, *args, **kwargs):
        """Call function ``f`` and refresh token if needed."""

        try:
            return f(*args, **kwargs)
        except requests.exceptions.HTTPError as exc:
            try:
                code = ElementTree.fromstring(exc.response.text)[0].text
            except Exception:
                # Any error here means the response was no XML
                try:
                    # Try to see if it's a json response, and if so, return it
                    exc.response.json()
                    return exc.response
                except Exception:
                    # Re-raise it, as it's not an expired token
                    raise exc
            # only catch 'token expired' exception
            # other codes may mean a different error
            if code not in ['900903', '900904']:
                raise
            self.client.token.refresh()
            return f(*args, **kwargs)

    def __call__(self, *args, **kwargs):

        def operation():
            f = self.get_operation()
            response = f(*args, **kwargs)
            response.raise_for_status()
            return response

        resp = self._with_refresh(operation)
        if resp.ok:
            # if response is raw file, return it directly
            if self.resource == 'files' and (self.operation == 'download'
                                             or self.operation == 'downloadFromDefaultSystem'):
                return resp
            result = self.post_process(resp.json(),
                                       self.return_type)['result']
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
            return resp.json()

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
