# agavepy test suite.
#
# To run the tests:
# 1. create a file, test_credentials.json, in the tests directory with credentials for accessing a tenant (see the ex).
#    Make sure to update: storage, storage_key, execution and execution_key and app_name
#
# 2. update the test-storage.json, test-compute.json, test-app.json and test-job.json
#
# 3. run with py.test from the cwd.
#

import datetime
import json
import os
import time

import pytest
import requests

import agavepy.agave as a
from agavepy.async import AgaveAsyncResponse
import testdata

HERE = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope='session')
def credentials():
    return json.load(open(
        os.path.join(HERE, 'test_credentials.json')))

@pytest.fixture(scope='session')
def agave(credentials):
    aga = a.Agave(username=credentials['username'],
                  password=credentials['password'],
                  api_server=credentials['apiserver'],
                  api_key=credentials['apikey'],
                  api_secret=credentials['apisecret'],
                  verify=credentials.get('verify_certs', True))
    aga.token.create()
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

def test_add_compute_system(agave, test_compute_system):
    system = agave.systems.add(body=test_compute_system)
    # set system as default for subsequent testing
    url = agave.api_server + '/systems/v2/' + test_compute_system['id']
    try:
        rsp = requests.put(url, data={'action':'setDefault'},
                           headers={'Authorization': 'Bearer ' + agave.token.token_info['access_token']},
                           verify=agave.verify)
    except requests.exceptions.HTTPError as exc:
        print "Error trying to register compute system:", str(exc)
        raise exc
    validate_system(system)

def test_add_storage_system(agave, test_storage_system):
    system = agave.systems.add(body=test_storage_system)
    # set system as default for subsequent testing
    url = agave.api_server + '/systems/v2/' + test_storage_system['id']
    try:
        rsp = requests.put(url, data={'action':'setDefault'},
                       headers={'Authorization': 'Bearer ' + agave.token.token_info['access_token']},
                       verify=agave.verify)
    except requests.exceptions.HTTPError as exc:
        print "Error trying to set storage system as default:", str(exc)
        raise exc
    validate_system(system)

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

def test_list_clients(agave):
    clients = agave.clients.list()
    for client in clients:
        validate_client(client)

def test_list_files(agave, credentials):
    files = agave.files.list(filePath=credentials['storage_user'], systemId=credentials['storage'])
    for file in files:
        validate_file(file)

def test_upload_file(agave, credentials):
    rsp = agave.files.importData(systemId=credentials['storage'],
                                 filePath=credentials['storage_user'],
                                 fileToUpload=open('test_file_upload_python_sdk', 'rb'))
    arsp = AgaveAsyncResponse(agave, rsp)
    status = arsp.result(timeout=120)
    assert status == 'COMPLETE'

def test_list_uploaded_file(agave, credentials):
    files = agave.files.list(filePath=credentials['storage_user'], systemId=credentials['storage'])
    for f in files:
        if 'test_file_upload_python_sdk' in f.path:
            break
    else:
        assert False

def test_delete_uploaded_file(agave, credentials):
    agave.files.delete(systemId=credentials['storage'],
                       filePath='{}/test_file_upload_python_sdk'.format(credentials['storage_user']))
    # make sure file isn't still there:
    files = agave.files.list(filePath=credentials['storage_user'], systemId=credentials['storage'])
    assert 'test_file_upload_python_sdk' not in [f.path for f in files]

def test_list_jobs(agave):
    jobs = agave.jobs.list()
    for job in jobs:
        validate_job(job)

def test_submit_job(agave, test_job):
    job = agave.jobs.submit(body=test_job)
    validate_job(job)

def test_get_profile(agave, credentials):
    prof = agave.profiles.get()
    validate_profile(prof, credentials['username'])

def test_list_profiles(agave, credentials):
    prof = agave.profiles.listByUsername(username='me')
    validate_profile(prof, credentials['username'])

def test_list_systems(agave):
    systems = agave.systems.list()
    for system in systems:
        validate_system(system)

def test_list_public_systems(agave):
    systems = agave.systems.list(public=True)
    for system in systems:
        validate_system(system)
        assert system.public

def test_list_default_systems(agave):
    systems = agave.systems.list(default=True)
    for system in systems:
        validate_system(system)
        assert system.default

def test_list_private_systems(agave):
    systems = agave.systems.list(public=False)
    for system in systems:
        validate_system(system)
        assert not system.public

def test_list_default_systems(agave):
    systems = agave.systems.list(default=True)
    for system in systems:
        validate_system(system)
        assert system.get('default')

def test_list_metadata(agave):
    md = agave.meta.listMetadata()
    assert len(md) > 0

def test_list_metadata_with_query(agave):
    md = agave.meta.listMetadata(q = "{'name': 'fooy'}")
    assert len(md) == 0

def test_add_list_delete_metadata(agave):
    # add a new one
    name = 'python-sdk-test-metadata'
    value = 'test value'
    d = {'name': name,
         'value': value}
    md = agave.meta.addMetadata(body=json.dumps(d))
    validate_meta(md, name, value)
    # find it in the list:
    mds = agave.meta.listMetadata(q = '')
    for md in mds:
        if md.name == 'python-sdk-test-metadata' and \
        md.value == 'test value':
            uuid = md.uuid
            break
    else:
        assert False
    # delete it
    md = agave.meta.deleteMetadata(uuid=uuid)
    # make sure it's really gone
    mds = agave.meta.listMetadata(q = '')
    assert not uuid in [md.uuid for md in mds]

def test_list_monitors(agave):
    ms = agave.monitors.list()
    for m in ms:
        validate_monitor(m)

def test_add_monitor(agave, credentials):
    body = {'active': True,
            'target': credentials['storage'],
            }
    m = agave.monitors.add(body=json.dumps(body))
    validate_monitor(m)
    # check monitor is in listing
    ms = agave.monitors.list()
    for m in ms:
        if m.target == credentials['storage']:
            break
    else:
        assert False

def test_delete_monitor(agave, credentials):
    # get monitor id from listing:
    ms = agave.monitors.list()
    for m in ms:
        if m.target == credentials['storage']:
            id = m.id
            break
    else:
        assert False
    agave.monitors.delete(monitorId=id)
    # make sure it is gone
    ms = agave.monitors.list()
    for m in ms:
        if m.target == credentials['storage']:
            assert False

def validate_notification(n):
    assert n.id
    assert n.event
    assert n.url

def test_list_notification(agave, credentials):
    # get uuid of storage system
    stor = agave.systems.get(systemId=credentials['storage'])
    assert stor.uuid
    ns = agave.notifications.list(associatedUuid=stor.uuid)
    for n in ns:
        validate_notification(n)

def test_create_notification(agave, credentials):
    # get uuid of storage system
    stor = agave.systems.get(systemId=credentials['storage'])
    assert stor.uuid
    body = {"associatedUuid": stor.uuid,
            "event": "*",
            "persistent": True,
            "url": "jstubbs@tacc.utexas.edu"
    }
    n = agave.notifications.add(body=json.dumps(body))
    validate_notification(n)
    # make sure it's there
    ns = agave.notifications.list(associatedUuid=stor.uuid)
    for nt in ns:
        if nt.id == n.id:
            break
    else:
        assert False

def test_delete_notification(agave, credentials):
    # get uuid of storage system
    stor = agave.systems.get(systemId=credentials['storage'])
    assert stor.uuid
    # list notifications
    ns = agave.notifications.list(associatedUuid=stor.uuid)
    assert len(ns) > 0
    id = ns[0].id
    agave.notifications.delete(uuid=id)
    # make sure it's actually gone
    ns = agave.notifications.list(associatedUuid=stor.uuid)
    for n in ns:
        if n.id == id:
            assert False

def test_notification_to_url(agave, credentials, test_storage_system):
    # first, create a request bin
    base_url = 'http://requestb.in/api/v1/bins'
    rsp = requests.post(base_url)
    bin_name = rsp.json().get('name')
    bin_url = '{}/{}'.format(base_url, bin_name)
    # create notification
     # get uuid of storage system
    stor = agave.systems.get(systemId=credentials['storage'])
    assert stor.uuid
    body = {"associatedUuid": stor.uuid,
            "event": "*",
            "persistent": True,
            "url": bin_url
    }
    n = agave.notifications.add(body=json.dumps(body))
    # wait for notification to be propagated
    time.sleep(3)
    # update the system:
    agave.systems.add(body=test_storage_system)
    # wait for notification to be sent
    # time.sleep(18)
    # # check for a notification
    # rsp = requests.get('{}/requests'.format(bin_url))
    # assert len(rsp.json()) > 0
    # delete the notification
    agave.notifications.delete(uuid=n.id)

def test_token_access(agave, credentials):
    token = agave.token.refresh()
    token_client = a.Agave(api_server=credentials['apiserver'],
                           token=token,
                           verify=credentials.get('verify_certs', True))
    apps = token_client.apps.list()
    for app in apps:
        validate_app(app)