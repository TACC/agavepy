from collections import Mapping, Sequence
from functools import wraps
import urlparse

import dateutil.parser
import requests

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


class Token(object):

    def __init__(self,
                 username, password,
                 api_server, api_key, api_secret,
                 parent):
        self.username = username
        self.password = password
        self.api_server = api_server
        self.api_key = api_key
        self.api_secret = api_secret
        # Agave object that created this token
        self.parent = parent

        self.token_url = urlparse.urljoin(self.api_server, 'token')

    def create(self):
        data = {'grant_type': 'password',
                'username': self.username,
                'password': self.password,
                'scope': 'PRODUCTION'}
        auth = requests.auth.HTTPBasicAuth(self.api_key, self.api_secret)
        resp = requests.post(self.token_url, data=data, auth=auth)
        resp.raise_for_status()
        self.token_info = resp.json()
        token = self.token_info['access_token']
        # Notify parent that a token was created
        self.parent._token = token
        self.parent.refresh_aris()
        return token


class AgaveError(Exception):
    pass


class Agave(object):

    PARAMS = [
        # param name, mandatory?, attr name
        ('username', False, 'username'),
        ('password', False, 'password'),
        ('api_server', True, 'api_server'),
        ('api_key', False, 'api_key'),
        ('api_secret', False, 'api_secret'),
        ('token', False, '_token'),
        ('resources', True, 'resources')
    ]

    def __init__(self, **kwargs):
        for param, mandatory, attr in self.PARAMS:
            try:
                value = kwargs[param] if mandatory else kwargs.get(param, None)
            except KeyError:
                raise AgaveError(
                    'parameter "{}" is mandatory'.format(param))
            setattr(self, attr, value)

        self.host = urlparse.urlsplit(self.api_server).netloc
        self.refresh_aris()

    def refresh_aris(self):
        self.clients_ari()
        self.token_ari()
        self.full_ari()

    def clients_ari(self):
        # If there is enough information to establish HTTP basic auth,
        # then create a 'clients' resource object
        self._clients = self.resource(
            'basic_auth', 'host', 'username', 'password')

    def full_ari(self):
        # If there is a token, then create a resource object with a
        # bearer token
        self.all = self.resource(
            'token', 'host', '_token')

    def token_ari(self):
        self.token = Token(
            self.username, self.password,
            self.api_server, self.api_key, self.api_secret,
            self)

    def resource(self, auth_type, *args):
        args_values = [getattr(self, arg) for arg in args]
        if all(args_values):
            http_client = SynchronousHttpClient()
            auth = getattr(http_client, 'set_{}'.format(auth_type))
            auth(*args_values)
            return SwaggerClient(
                self.resources, http_client=http_client,
                extra_processors=[AgaveProcessor()])

    def __getattr__(self, key):
        base = self._clients if key == 'clients' else self.all
        resource = getattr(base, key)
        return Resource(resource,
                        models=resource.json['api_declaration']['models'])


class Resource(object):

    def __init__(self, obj, models):
        self.obj = obj
        self.models = models

    def __getattr__(self, attr):
        operation = getattr(self.obj, attr)
        return_type = operation.json
        return Operation(operation, return_type, self.models)


class Operation(object):

    PRIMITIVE_TYPES = ['array', 'string', 'integer', 'boolean']

    def __init__(self, operation, return_type, models):
        self.operation = operation
        self.return_type = return_type
        self.models = models

    def __call__(self, *args, **kwargs):
        resp = self.operation(*args, **kwargs)
        resp.raise_for_status()
        return self.post_process(resp.json(), self.return_type)['result']

    def post_process(self, obj, return_type):
        if return_type is None:
            return self.process_untyped(obj)
        type_name = return_type['type']
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
