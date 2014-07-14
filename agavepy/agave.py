from collections import Mapping, Sequence
from functools import wraps
import urlparse

import requests

from swaggerpy.client import SwaggerClient
from swaggerpy.http_client import SynchronousHttpClient


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
        self.clients = self.resource(
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
                self.resources, http_client=http_client)

    def __getattr__(self, key):
        return Wrapper(getattr(self.all, key))


class Wrapper(object):

    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, attr):
        return Wrapper(getattr(self.obj, attr))

    def __call__(self, *args, **kwargs):
        resp = self.obj(*args, **kwargs)
        resp.raise_for_status()
        return wrap(resp.json()['result'])


def wrap(obj):
    if isinstance(obj, basestring):
        return obj
    if isinstance(obj, Mapping):
        return AttrDict({key:wrap(value) for key, value in obj.items()})
    if isinstance(obj, Sequence):
        return [wrap(item) for item in obj]
    return obj


class AttrDict(dict):

    def __getattr__(self, key):
        return self[key]
