import datetime
import json
import os
import time

import pytest
import requests

import agavepy.agave as a
from agavepy.async import AgaveAsyncResponse
from . import testdata

HERE = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session')
def credentials():
    '''
    Load credentials for testing session

    Order: user credential store, test file, env
    '''
    credentials = {}
    # credential store
    ag_cred_store = os.path.expanduser('~/.agave/current')
    if os.path.exists(ag_cred_store):
        tempcred = json.load(open(ag_cred_store, 'r'))
        credentials['apiserver'] = tempcred.get('baseurl', None)
        credentials['username'] = tempcred.get('username', None)
        credentials['password'] = tempcred.get('password', None)
        credentials['apikey'] = tempcred.get('apikey', None)
        credentials['apisecret'] = tempcred.get('apisecret', None)
        credentials['token'] = tempcred.get('access_token', None)
        credentials['refresh_token'] = tempcred.get('refresh_token', None)
        credentials['verify_certs'] = tempcred.get('verify', None)
        credentials['client_name'] = tempcred.get('client_name', None)
        credentials['tenantid'] = tempcred.get('tenantid', None)
    # test file
    credentials_file = os.environ.get('creds', 'test_credentials.json')
    print(("Loading file: {}".format(credentials_file)))
    if os.path.exists(credentials_file):
        credentials = json.load(open(
            os.path.join(HERE, credentials_file), 'r'))
    # environment
    for env in ('apikey', 'apisecret', 'username', 'password',
                'apiserver', 'verify_certs', 'refresh_token',
                'token', 'client_name'):
        varname = '_AGAVE_' + env.upper()
        if os.environ.get(varname, None) is not None:
            credentials[env] = os.environ.get(varname)
            print("Loaded {} from env".format(env))

    return credentials


@pytest.fixture(scope='session')
def agave(credentials):
    aga = a.Agave(username=credentials.get('username'),
                  password=credentials.get('password'),
                  api_server=credentials.get('apiserver'),
                  api_key=credentials.get('apikey'),
                  api_secret=credentials.get('apisecret'),
                  token=credentials.get('token'),
                  refresh_token=credentials.get('refresh_token'),
                  verify=credentials.get('verify_certs', True))
    return aga


def test_profiles_username(agave, credentials):
    '''verify that agavepy and testing view of username is same'''
    username = agave.profiles.get()['username']
    assert credentials['username'] == username
