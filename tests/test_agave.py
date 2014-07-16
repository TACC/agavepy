import datetime
import json

import pytest

import agavepy.agave as a
import testdata

@pytest.fixture(scope='session')
def credentials():
    return json.load(open('test_credentials.json'))

@pytest.fixture(scope='session')
def agave(credentials):
    aga = a.Agave(resources=credentials['resources'],
                  username=credentials['username'],
                  password=credentials['password'],
                  api_server=credentials['apiserver'],
                  api_key=credentials['apikey'],
                  api_secret=credentials['apisecret'])
    aga.token.create()
    return aga

@pytest.fixture(scope='session')
def test_app(credentials):
    return testdata.TestData(credentials).get_test_app()

@pytest.fixture(scope='session')
def test_job(credentials):
    return testdata.TestData(credentials).get_test_job()

@pytest.fixture(scope='session')
def test_compute_system(credentials):
    return testdata.TestData(credentials).get_test_compute_system()

@pytest.fixture(scope='session')
def test_storage_system(credentials):
    return testdata.TestData(credentials).get_test_storage_system()

def validate_app(app):
    assert app.id
    assert app.executionSystem
    assert type(app.lastModified) is datetime.datetime
    assert app.name
    assert type(app.revision) is int and app.revision > 0
    assert app.version

def test_list_apps(agave):
    apps = agave.apps.list()
    for app in apps:
        validate_app(app)

def test_list_public_apps(agave):
    apps = agave.apps.list(publicOnly=True)
    for app in apps:
        validate_app(app)
        assert app.isPublic

def test_list_private_apps(agave):
    apps = agave.apps.list(privateOnly=True)
    for app in apps:
        validate_app(app)
        assert not app.isPublic

def test_add_app(agave, test_app):
    app = agave.apps.add(body=test_app)
    validate_app(app)

def validate_client(client):
    assert client.consumerKey

def test_list_clients(agave):
    clients = agave.clients.list()
    for client in clients:
        validate_client(client)

def validate_file(file):
    assert file.format
    assert type(file.lastModified) is datetime.datetime
    assert type(file.length) is int
    assert file.mimeType
    assert file.name
    assert file.path
    assert file.system

def test_list_files(agave, credentials):
    files = agave.files.listOnDefaultSystem(filePath=credentials['username'])
    for file in files:
        validate_file(file)

def validate_job(job):
    assert job.appId
    if 'endTime' in job:
        assert job.endTime is None or  type(job.endTime) is datetime.datetime
    assert job.executionSystem
    assert job.id
    assert job.name
    assert job.owner
    if 'startTime' in job:
        assert job.startTime is None or type(job.startTime) is datetime.datetime
    assert job.status

def test_list_jobs(agave):
    jobs = agave.jobs.list()
    for job in jobs:
        validate_job(job)

def test_submit_job(agave, test_job):
    job = agave.jobs.submit(body=test_job)
    validate_job(job)

def validate_system(system):
    assert type(system.public) is bool
    assert system.name
    assert system.status
    assert system.type

def test_list_systems(agave):
    systems = agave.systems.list()
    for system in systems:
        validate_system(system)

def test_list_public_systems(agave):
    systems = agave.systems.list(publicOnly=True)
    for system in systems:
        validate_system(system)
        assert system.public

def test_list_private_systems(agave):
    systems = agave.systems.list(privateOnly=True)
    for system in systems:
        validate_system(system)
        assert not system.public

def test_list_default_systems(agave):
    systems = agave.systems.list(default=True)
    for system in systems:
        validate_system(system)
        assert system.default

def test_add_compute_system(agave, test_compute_system):
    system = agave.systems.add(body=test_compute_system)
    validate_system(system)

def test_add_storage_system(agave, test_storage_system):
    system = agave.systems.add(body=test_storage_system)
    validate_system(system)

def test_token_access(agave, credentials):
    token = agave.token.refresh()
    token_client = a.Agave(
        resources=credentials['resources'],
        api_server=credentials['apiserver'],
        token=token)
    apps = token_client.apps.list()
    for app in apps:
        validate_app(app)