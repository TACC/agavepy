# agavepy test suite.
#
# To run the tests:
# 1. create a file, test_credentials.json, in the tests directory with credentials for accessing a tenant (see the ex).
#    Make sure to update: storage, storage_key, execution and execution_key and app_name
#
# 2. update the test-storage.json, test-compute.json, test-app.json and test-job.json
#
# 3. To run the tests, use the following from the tests directory with the requirements.txt installed (or activate a
#    virtualenv with the requirements):
#
#    py.test                            -- Run all tests
#    py.test test_agave.py::<test_name> -- Run a single test whose name is <test_name>
#    py.test -k <string>                -- Run all tests with <string> in the name.
#
#    Examples:
#    py.test test_agave.py::test_list_single_job_many_times
#    py.test -k jobs

import datetime
import json
import os
import time

import pytest
import requests

import agavepy.agave as a
from agavepy.asynchronous import AgaveAsyncResponse
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
    if os.environ.get('AGAVE_CACHE_DIR', None) is not None:
        ag_cred_store = os.path.join(os.environ.get('AGAVE_CACHE_DIR'),
                                     'current')
    else:
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
        credentials = json.load(open(os.path.join(HERE, credentials_file),
                                     'r'))
    # environment
    for env in ('apikey', 'apisecret', 'username', 'password', 'apiserver',
                'verify_certs', 'refresh_token', 'token', 'client_name',
                'tenantid'):
        for varname_root in ['_AGAVE_', 'AGAVE_']:
            varname = varname_root + env.upper()
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


@pytest.fixture(scope='session')
def test_app(credentials):
    return testdata.TestData(credentials).get_test_app_from_file()


@pytest.fixture(scope='session')
def test_job(credentials):
    return testdata.TestData(credentials).get_test_job_from_file()


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


def validate_client(client):
    pass
    # todo - this should turned back on when the clients service is working again.
    # assert client.consumerKey


def validate_file(file):
    assert file.format
    assert type(file.lastModified) is datetime.datetime
    assert type(file.length) is int
    assert file.mimeType
    assert file.name
    assert file.path
    assert file.system


def validate_history_rec(rec):
    assert rec.description


def validate_job(job):
    assert job.appId
    if 'endTime' in job:
        assert job.endTime is None or type(job.endTime) is datetime.datetime
    assert job.executionSystem
    assert job.id
    assert job.name
    assert job.owner
    if 'startTime' in job:
        assert job.startTime is None or type(
            job.startTime) is datetime.datetime
    assert job.status


def validate_system(system):
    assert type(system.public) is bool
    assert system.name
    assert system.status
    assert system.type


def validate_profile(prof, user):
    assert prof.username == user


def validate_meta(md, name, value):
    assert md.name == name
    assert md.value == value


def validate_monitor(m):
    assert m.id
    assert m.target
    assert m.frequency


def validate_file_pem(pem):
    assert pem.permission
    assert 'execute' in pem.permission
    assert 'read' in pem.permission
    assert 'write' in pem.permission


# def test_transfer_file(agave, credentials):
#     agave.files.importData(systemId=credentials['storage'],
#                            filePath=credentials['storage_user'],
#                            fileName='test_file_upload_python_sdk',
#                            urlToIngest='agave://{}/{}/test_dest_transfer_python_sdk'.format(credentials['storage'],
#                                                               credentials['storage_user']))


def test_metadata_admin_pems(agave, credentials):
    # first, lets add a new metadata using the normal user's client
    name = 'python-sdk-test-metadata-admin-pems'
    value = 'test value'
    d = {'name': name, 'value': value}
    md = agave.meta.addMetadata(body=json.dumps(d))
    uuid = md.uuid
    # let's make sure it is there
    md2 = agave.meta.listMetadata(q=json.dumps({'name': name}))
    assert uuid in [md.uuid for md in md2]
    # now, create a new client representing the admin
    ag = a.Agave(username=credentials.get('admin_username'),
                 password=credentials.get('admin_password'),
                 api_server=credentials.get('apiserver'),
                 api_key=credentials.get('apikey'),
                 api_secret=credentials.get('apisecret'),
                 token=credentials.get('token'),
                 refresh_token=credentials.get('refresh_token'),
                 verify=credentials.get('verify_certs', True))
    # let's check that the admin can see our metadata
    md2 = ag.meta.listMetadata(q=json.dumps({'name': name}))
    assert uuid in [md.uuid for md in md2]
    # now, explicitly turn off 'implicit' permissions
    md3 = ag.meta.listMetadata(q=json.dumps({'name': name}), privileged=False)
    assert uuid not in [md.uuid for md in md3]
    # finally, delete the original metadata
    agave.meta.deleteMetadata(uuid=uuid)
