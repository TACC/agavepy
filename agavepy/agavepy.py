#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

AgavePy
=======

Very basic wrapper for requests to play with the Agave API.

"""

import json
import os
import shelve
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
        return resp.json()
    return _verb


class AgaveAPI(object):

    BASE = 'https://agave.iplantc.org'

    def __init__(self, user, password, tenant=None):
        self.user = user
        self.password = password
        self.tenant = tenant or self.BASE
        self.auth = requests.auth.HTTPBasicAuth(self.user, self.password)
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

    GET = verb('get')
    POST = verb('post')
    DELETE = verb('delete')

    def clients_create(self, client_name, **kwargs):
        url = self._url('clients/v2')
        data = {'clientName': client_name,
                'tier': 'Unlimited'}
        data.update(kwargs)
        resp = self.POST(url, data=data, auth=self.auth)
        if resp['status'] == 'success':
            self.clients[resp['result']['name']] = {'response': resp['result']}
        return resp

    def clients_list(self):
        url = self._url('clients/v2')
        return self.GET(url, auth=self.auth)

    def clients_info(self, client_name):
        url = self._url('clients/v2', client_name, auth=self.auth)
        return self.GET(url)

    def clients_delete(self, client_name):
        url = self._url('clients/v2', client_name)
        return self.DELETE(url, auth=self.auth)

    def token(self, client):
        url = self._url('token')
        data = {'grant_type': 'client_credentials',
                'username': self.user,
                'password': self.password,
                'scope': 'PRODUCTION'}
        client_data = self.clients[client]
        consumer_key = client_data['response']['consumerKey']
        consumer_secret = client_data['response']['consumerSecret']
        auth = requests.auth.HTTPBasicAuth(consumer_key, consumer_secret)
        resp = self.POST(url, data=data, auth=auth)
        # use temp, or set writeback=True
        temp = self.clients[client]
        temp['token'] = resp
        self.clients[client] = temp
        return resp

    def bearer(self, token):
        return {'Authorization': 'Bearer {}'.format(token)}

    def systems_list(self, client):
        token = self.clients[client]['token']['access_token']
        url = self._url('systems/v2')
        return self.GET(url, headers=self.bearer(token))

    def systems_create(self, client, system_data):
        token = self.clients[client]['token']['access_token']
        url = self._url('systems/v2')
        files = {'fileToUpload': json.dumps(system_data)}
        return self.POST(url, headers=self.bearer(token), files=files)