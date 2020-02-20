__author__ = 'vaughn'

from pprint import pprint
import datetime
import json
import os
import time
import tempfile

import pytest
import requests

import agavepy.agave as a
import agavepy.constants as constants
import agavepy.settings as settings
from .data import keys as sshkeys
from agavepy.asynchronous import AgaveAsyncResponse
from .data.integration import (MockData, TEST_UPLOAD_BINARY_FILE,
                               TEST_UPLOAD_FILE, TEST_UPLOAD_TIMEOUT)

HERE = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session')
def syshost():
    return 'systemhost.tacc.cloud'


@pytest.fixture(scope='session')
def execution_system_id():
    return 'test-execution-tacc-prod'


@pytest.fixture(scope='session')
def storage_system_id():
    return 'test-storage-tacc-prod'


@pytest.fixture(scope='session')
def sysuser():
    return 'ubuntu'


@pytest.fixture(scope='session')
def syspubkey():
    if os.environ.get('TEST_TAPIS_PUBKEY', None) is not None:
        return sshkeys.b64decode(os.environ.get('TEST_TAPIS_PUBKEY'))
    else:
        return sshkeys.pubkey_from_file()


@pytest.fixture(scope='session')
def sysprivkey():
    if os.environ.get('TEST_TAPIS_PRIVKEY', None) is not None:
        return sshkeys.b64decode(os.environ.get('TEST_TAPIS_PRIVKEY'))
    else:
        return sshkeys.privkey_from_file()


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
    return MockData(credentials).get_test_app_from_file()


@pytest.fixture(scope='session')
def test_job(credentials):
    return MockData(credentials).get_test_job_from_file()


@pytest.fixture(scope='session')
def test_compute_system(credentials, execution_system_id, syshost, sysuser,
                        syspubkey, sysprivkey):
    return MockData(credentials).get_test_compute_system(
        execution_system_id, syshost, sysuser, syspubkey, sysprivkey)


@pytest.fixture(scope='session')
def test_storage_system(credentials, storage_system_id, syshost, sysuser,
                        syspubkey, sysprivkey):
    return MockData(credentials).get_test_storage_system(
        storage_system_id, syshost, sysuser, syspubkey, sysprivkey)


@pytest.fixture(scope='session')
def test_pem_username():
    return 'cicsvc'


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


def test_add_compute_system(agave, test_compute_system):
    system = agave.systems.add(body=test_compute_system)
    # set system as default for subsequent testing
    url = agave.api_server + '/systems/v2/' + test_compute_system['id']
    try:
        rsp = requests.put(url,
                           data={'action': 'setDefault'},
                           headers={'Authorization': 'Bearer ' + agave._token},
                           verify=agave.verify)
    except requests.exceptions.HTTPError as exc:
        print(("Error trying to register compute system:", str(exc)))
        raise exc
    validate_system(system)


def test_add_storage_system(agave, test_storage_system):
    system = agave.systems.add(body=test_storage_system)
    # set system as default for subsequent testing
    url = agave.api_server + '/systems/v2/' + test_storage_system['id']
    try:
        rsp = requests.put(url,
                           data={'action': 'setDefault'},
                           headers={'Authorization': 'Bearer ' + agave._token},
                           verify=agave.verify)
    except requests.exceptions.HTTPError as exc:
        print(("Error trying to set storage system as default:", str(exc)))
        raise exc
    validate_system(system)


def test_list_compute_system(agave, execution_system_id):
    files = agave.files.list(systemId=execution_system_id, filePath='/')
    for f in files:
        validate_file(f)


def test_list_storage_system(agave, storage_system_id):
    files = agave.files.list(systemId=storage_system_id, filePath='/')
    for f in files:
        validate_file(f)


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


# def test_add_app(agave, test_app):
#     app = agave.apps.add(body=test_app)
#     validate_app(app)


def test_list_clients(agave, credentials):
    if not credentials.get('username') or not credentials.get('password'):
        print("Skipping test_list_clients")
        return
    clients = agave.clients.list()
    for client in clients:
        validate_client(client)


def test_files_mkdir(agave, storage_system_id, test_username):
    adir = agave.files.manage(systemId=storage_system_id,
                              body={
                                  'action': 'mkdir',
                                  'path': test_username
                              },
                              filePath='/')
    assert adir['uuid']
    assert adir['name']
    assert adir['owner']


def test_list_files(agave, storage_system_id, test_username):
    files = agave.files.list(filePath=test_username,
                             systemId=storage_system_id)
    for file in files:
        validate_file(file)


def test_get_file_history(agave, storage_system_id, test_username):
    history = agave.files.getHistory(filePath=test_username,
                                     systemId=storage_system_id)
    for rec in history:
        validate_history_rec(rec)


def test_list_file_pems(agave, storage_system_id, test_username):
    pems = agave.files.listPermissions(filePath=test_username,
                                       systemId=storage_system_id)
    for pem in pems:
        validate_file_pem(pem)


def test_add_file_permissions(agave, storage_system_id, test_username,
                              test_pem_username):
    body = {
        'permission': 'ALL',
        'recursive': False,
        'username': test_pem_username
    }
    pems = agave.files.updatePermissions(systemId=storage_system_id,
                                         filePath=test_username,
                                         body=body)
    for pem in pems:
        validate_file_pem(pem)


def test_update_file_pems(agave, storage_system_id, test_username,
                          test_pem_username):
    body = {
        'permission': 'READ',
        'recursive': False,
        'username': test_pem_username
    }
    rsp = agave.files.updatePermissions(systemId=storage_system_id,
                                        filePath=test_username,
                                        body=body)


def test_upload_file(agave, storage_system_id, test_username):
    rsp = agave.files.importData(systemId=storage_system_id,
                                 filePath=test_username,
                                 fileToUpload=open(TEST_UPLOAD_FILE, 'rb'))
    arsp = AgaveAsyncResponse(agave, rsp)
    status = arsp.result(timeout=TEST_UPLOAD_TIMEOUT)
    assert status == 'FINISHED'


def test_download_file(agave, storage_system_id, test_username):
    rsp = agave.files.download(systemId=storage_system_id,
                               filePath='{0}/{1}'.format(
                                   test_username,
                                   os.path.basename(TEST_UPLOAD_FILE)))
    assert rsp.status_code == 200


def test_upload_binary_file(agave, storage_system_id, test_username):
    rsp = agave.files.importData(systemId=storage_system_id,
                                 filePath=test_username,
                                 fileToUpload=open(TEST_UPLOAD_BINARY_FILE,
                                                   'rb'))
    arsp = AgaveAsyncResponse(agave, rsp)
    status = arsp.result(timeout=TEST_UPLOAD_TIMEOUT)
    assert status == 'FINISHED'


def test_download_binary_file(agave, storage_system_id, test_username):
    rsp = agave.files.download(systemId=storage_system_id,
                               filePath='{0}/{1}'.format(
                                   test_username,
                                   os.path.basename(TEST_UPLOAD_BINARY_FILE)))
    assert rsp.status_code == 200


def test_download_agave_uri(agave, storage_system_id, test_username):
    remote_path = '{}/test_file_upload_python_sdk'.format(test_username)
    local_path = tempfile.mkstemp()[1]
    uri = 'agave://{}/{}'.format(storage_system_id, remote_path)
    rsp = agave.download_uri(uri, local_path)
    assert os.path.exists(local_path)
    os.remove(local_path)


def test_list_uploaded_file(agave, storage_system_id, test_username):
    files = agave.files.list(filePath='{0}/{1}'.format(
        test_username, os.path.basename(TEST_UPLOAD_FILE)),
                             systemId=storage_system_id)
    for f in files:
        if os.path.basename(TEST_UPLOAD_FILE) in f.path:
            break
    else:
        assert False


def test_list_uploaded_binary_file(agave, storage_system_id, test_username):
    files = agave.files.list(filePath='{0}/{1}'.format(
        test_username, os.path.basename(TEST_UPLOAD_BINARY_FILE)),
                             systemId=storage_system_id)
    for f in files:
        if os.path.basename(TEST_UPLOAD_BINARY_FILE) in f.path:
            break
    else:
        assert False


def test_delete_uploaded_files(agave, storage_system_id, test_username):
    uploaded_files = [
        os.path.basename(TEST_UPLOAD_BINARY_FILE),
        os.path.basename(TEST_UPLOAD_FILE)
    ]
    for f in uploaded_files:
        agave.files.delete(systemId=storage_system_id,
                           filePath='{}/{}'.format(test_username, f))
        # make sure file isn't still there:
        files = agave.files.list(filePath=test_username,
                                 systemId=storage_system_id)
        assert f not in [fl.path for fl in files]


########
# Jobs #
########


def test_list_jobs(agave):
    jobs = agave.jobs.list()
    for job in jobs:
        validate_job(job)
    assert len(jobs) > 0, 'User has no listable jobs'


def test_list_single_job_many_times(agave):
    jobs = agave.jobs.list()
    if len(jobs) > 0:
        job = jobs[0]
        for i in range(1, 15):
            j = agave.jobs.get(jobId=job.id)
            validate_job(j)
    else:
        raise ValueError('User has no listable jobs')
