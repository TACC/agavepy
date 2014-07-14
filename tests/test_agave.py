import json

import pytest

import agavepy.agave as a


@pytest.fixture(scope='session')
def agave(request):
    credentials = json.load(open('test_credentials.json'))
    aga = a.Agave(resources=credentials['resources'],
                  username=credentials['username'],
                  password=credentials['password'],
                  api_server=credentials['apiserver'],
                  api_key=credentials['apikey'],
                  api_secret=credentials['apisecret'])
    aga.token.create()
    return aga

def validate(app):
    assert app.id
    assert app.executionSystem

def test_lisp_apps(agave):
    apps = agave.apps.list()
    for app in apps:
        validate(app)
