#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

EasyRest
========

Very basic wrapper for requests to play with the Agave API.

"""

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
        self.clients = shelve.open(os.path.expanduser('~/.agave_clients'))

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