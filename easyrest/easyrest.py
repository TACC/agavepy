#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

EasyRest
========

Very basic wrapper for requests to play with the Agave API.

"""

import os
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

    def _url(self, *args):
        return urllib.parse.urljoin(self.BASE, os.path.join(*args))

    GET = verb('get')
    POST = verb('post')

    def clients_create(self, client_name):
        url = self._url('clients/v2')
        data = {'clientName': client_name,
                'tier': 'Unlimited'}
        return self.POST(url, data=data)

    def clients_list(self):
        url = self._url('clients/v2')
        return self.GET(url)
