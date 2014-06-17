#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

AgavePy
=======

Very basic wrapper for requests to play with the Agave API.

"""

import functools
import json
import os
import shelve
import time
import urllib

import requests


def verb(verb_name):
    """Construct an HTTP verb.

    Save the response as `last_response`, for debugging purposes.

    """
    def _verb(self, *args, **kwargs):
        fun = getattr(requests, verb_name)
        resp = fun(*args, **kwargs)
        self.last_response = resp
        if not resp.ok:
            raise Exception(resp.text)
        return resp.json()
    return _verb


def method(verb):
    """Make an already authorized method.

    Use as::

        @method('GET')
        def foo(self, method, arg1, kwarg='bar'):
            ...
            method(url, ...)

    and invoke as::

        a_client.foo(arg1, kwarg='')

    """

    def decorator(f):
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            client = kwargs.pop('client', self.default_client)
            token = self.token(client)
            headers = kwargs.pop('headers', {})
            headers.update(self.bearer(token))
            meth = functools.partial(getattr(self, verb), headers=headers)
            return f(self, meth, *args, **kwargs)
        return wrapper
    return decorator


def optional_system(system):
    if system is None:
        return ''
    return 'system/{}'.format(system)


class AgaveAPI(object):

    BASE = 'https://agave.iplantc.org'

    def __init__(self, user, password, tenant=None, client=None):
        self.user = user
        self.password = password
        self.tenant = tenant or self.BASE
        self.auth = requests.auth.HTTPBasicAuth(self.user, self.password)
        self.default_client = client
        self.load_persistent_data()

    @property
    def persistent_data_filename(self):
        tenant = urllib.parse.urlparse(self.tenant).netloc
        return os.path.join(self.persistent_data_dir,
                            '{}_{}'.format(self.user, tenant))

    @property
    def persistent_data_dir(self):
        dot_dir = os.path.expanduser('~/.agave_clients')
        os.makedirs(dot_dir, exist_ok=True)
        return dot_dir

    def load_persistent_data(self):
        self.clients = shelve.open(self.persistent_data_filename, flag='c')

    def _url(self, *args):
        return urllib.parse.urljoin(self.tenant, os.path.join(*args))

    def bearer(self, token):
        return {'Authorization': 'Bearer {}'.format(token)}

    GET = verb('get')
    POST = verb('post')
    PUT = verb('put')
    DELETE = verb('delete')

    # --- Token ---

    def _get_token(self, client):
        """Request a token by sending credentials."""

        url = self._url('token')
        data = {'grant_type': 'password',
                'username': self.user,
                'password': self.password,
                'scope': 'PRODUCTION'}
        client_data = self.clients[client]
        consumer_key = client_data['response']['consumerKey']
        consumer_secret = client_data['response']['consumerSecret']
        auth = requests.auth.HTTPBasicAuth(consumer_key, consumer_secret)
        return self.POST(url, data=data, auth=auth)

    def _refresh_token(self, client):
        """Refresh token from cache info."""

        url = self._url('token')
        client_data = self.clients[client]
        refresh_token = client_data['token']['refresh_token']
        data = {'grant_type': 'refresh_token',
                'scope': 'PRODUCTION',
                'refresh_token': refresh_token}
        consumer_key = client_data['response']['consumerKey']
        consumer_secret = client_data['response']['consumerSecret']
        auth = requests.auth.HTTPBasicAuth(consumer_key, consumer_secret)
        return self.POST(url, data=data, auth=auth)

    def token(self, client):
        "Do as possible to get a valid token for this client."

        client_data = self.clients[client]
        try:
            token_data = client_data['token']
        except KeyError:
            # we haven't got a token for this client yet
            # so get a fresh one
            token_data = self._get_token(client)
            token_data['created'] = time.time()
            client_data['token'] = token_data
            self.clients[client] = client_data

        if time.time() >= token_data['created'] + token_data['expires_in']:
            token_data = self._refresh_token(client)

        return token_data['access_token']

    def reset_token(self, client):
        try:
            client_data =  self.clients[client]
            del client_data['token']
            self.clients[client] = client_data
        except KeyError:
            pass
        return self.token(client)

    # --- Clients ---

    def clients_create(self, client_name, **kwargs):
        url = self._url('clients/v2')
        data = {'clientName': client_name,
                'tier': 'Unlimited'}
        data.update(kwargs)
        resp = self.POST(url, data=data, auth=self.auth)
        if resp['status'] == 'success':
            self.clients[resp['result']['name']] = {'response': resp['result']}
        return resp

    def clients_list(self, **kwargs):
        url = self._url('clients/v2', **kwargs)
        return self.GET(url, auth=self.auth)

    def clients_info(self, client_name):
        url = self._url('clients/v2', client_name)
        return self.GET(url, auth=self.auth)

    def clients_delete(self, client_name):
        url = self._url('clients/v2', client_name)
        return self.DELETE(url, auth=self.auth)

    # --- Systems ---

    @method('GET')
    def systems_list(self, method, **kwargs):
        url = self._url('systems/v2')
        return method(url, params=kwargs)

    @method('POST')
    def systems_add(self, method, filename):
        url = self._url('systems/v2')
        with open(filename) as f:
            return method(url, files={'fileToUpload': f})

    @method('GET')
    def systems_info(self, method, system):
        url = self._url('systems/v2', system)
        return method(url)

    @method('POST')
    def systems_create(self, method, system_data):
        url = self._url('systems/v2')
        files = {'fileToUpload': json.dumps(system_data)}
        return method(url, files=files)

    @method('PUT')
    def systems_make_default(self, method, system):
        url = self._url('systems/v2', system)
        data = {'action': 'setDefault'}
        return method(url, data=data)

    # --- Files ---


    @method('GET')
    def listings(self, method, path, system=None):
        url = self._url('files/v2/listings', optional_system(system), path)
        return method(url)

    @method('GET')
    def pems(self, method, path, system=None):
        url = self._url('files/v2/pems', optional_system(system), path)
        return method(url)

    @method('POST')
    def pems_update(self, method, path, system=None, **kwargs):
        data = {'username': 'public', 'read': True}
        url = self._url('files/v2/pems', optional_system(system), path)
        return method(url, data=data)

    # --- Apps ---

    @method('GET')
    def apps_list(self, method, **kwargs):
        url = self._url('apps/v2/')
        return method(url, params=kwargs)

    @method('POST')
    def apps_create(self, method, app_data):
        url = self._url('apps/v2/')
        return method(url,
                      files={'fileToUpload': json.dumps(app_data)})