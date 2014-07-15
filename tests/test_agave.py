import datetime
import json

import pytest

import agavepy.agave as a
import testdata

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

@pytest.fixture(scope='session')
def test_app():
    credentials = json.load(open('test_credentials.json'))
    return testdata.TestData(credentials).get_test_app()

def validate(app):
    assert app.id
    assert app.executionSystem
    assert type(app.lastModified) is datetime.datetime
    assert app.name
    assert type(app.revision) is int and app.revision > 0
    assert app.version

def test_list_apps(agave):
    apps = agave.apps.list()
    for app in apps:
        validate(app)

def test_list_public_apps(agave):
    apps = agave.apps.list(publicOnly=True)
    for app in apps:
        validate(app)
        assert app.isPublic

def test_list_private_apps(agave):
    apps = agave.apps.list(privateOnly=True)
    for app in apps:
        validate(app)
        assert not app.isPublic

def test_add_app(agave, test_app):
    app = agave.apps.add(body=test_app)
    validate(app)
