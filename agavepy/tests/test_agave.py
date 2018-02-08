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
        rsp = requests.put(url, data={'action':'setDefault'},
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
        rsp = requests.put(url, data={'action':'setDefault'},
                       headers={'Authorization': 'Bearer ' + agave._token},
                       verify=agave.verify)
    except requests.exceptions.HTTPError as exc:
        print(("Error trying to set storage system as default:", str(exc)))
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

def test_list_clients(agave, credentials):
    if not credentials.get('username') or not credentials.get('password'):
        print("Skipping test_list_clients")
        return
    clients = agave.clients.list()
    for client in clients:
        validate_client(client)

def test_list_files(agave, credentials):
    files = agave.files.list(filePath=credentials['storage_user'], systemId=credentials['storage'])
    for file in files:
        validate_file(file)

def test_get_file_history(agave, credentials):
    history = agave.files.getHistory(filePath=credentials['storage_user'], systemId=credentials['storage'])
    for rec in history:
        validate_history_rec(rec)

def test_list_file_pems(agave, credentials):
    pems = agave.files.listPermissions(filePath=credentials['storage_user'], systemId=credentials['storage'])
    for pem in pems:
        validate_file_pem(pem)

def test_add_file_permissions(agave, credentials):
    body = {'permission': 'ALL',
            'recursive': True,
            'username': 'jstubbs'}
    pems = agave.files.updatePermissions(systemId=credentials['storage'],
                                         filePath=credentials['storage_user'], body=body)
    for pem in pems:
        validate_file_pem(pem)

def test_update_file_pems(agave, credentials):
    body = {'permission': 'READ', 'recursive': False, 'username': credentials['storage_user']}
    rsp = agave.files.updatePermissions(systemId=credentials['storage'],
                                        filePath=credentials['storage_user'],
                                        body=body)

def test_upload_file(agave, credentials):
    rsp = agave.files.importData(systemId=credentials['storage'],
                                 filePath=credentials['storage_user'],
                                 fileToUpload=open('test_file_upload_python_sdk', 'rb'))
    arsp = AgaveAsyncResponse(agave, rsp)
    status = arsp.result(timeout=120)
    assert status == 'FINISHED'

def test_download_file(agave, credentials):
    rsp = agave.files.download(systemId=credentials['storage'],
                               filePath='{}/test_file_upload_python_sdk'.format(credentials['storage_user']))
    assert rsp.status_code == 200

def test_download_file_range(agave, credentials):
    rsp = agave.files.download(systemId=credentials['storage'],
                               filePath='{}/test_file_upload_python_sdk'.format(credentials['storage_user']),
                               headers={'range': 'bytes=1-5'}
                               )
    assert rsp.status_code == 200

# def test_transfer_file(agave, credentials):
#     agave.files.importData(systemId=credentials['storage'],
#                            filePath=credentials['storage_user'],
#                            fileName='test_file_upload_python_sdk',
#                            urlToIngest='agave://{}/{}/test_dest_transfer_python_sdk'.format(credentials['storage'],
#                                                               credentials['storage_user']))

def test_upload_binary_file(agave, credentials):
    rsp = agave.files.importData(systemId=credentials['storage'],
                                 filePath=credentials['storage_user'],
                                 fileToUpload=open('test_upload_python_sdk_g_art.mov', 'rb'))
    arsp = AgaveAsyncResponse(agave, rsp)
    status = arsp.result(timeout=120)
    assert status == 'FINISHED'

def test_download_agave_uri(agave, credentials):
    remote_path = '{}/test_file_upload_python_sdk'.format(credentials['storage_user'])
    local_path = os.path.join(HERE, 'local_test_download')
    uri = 'agave://{}/{}'.format(credentials['storage'], remote_path)
    rsp = agave.download_uri(uri, local_path)
    assert os.path.exists(local_path)
    os.remove(local_path)

def test_download_job_output_listings_uri(agave):
    # this test currently does not work on other tenants.
    # todo - update to make tenant-agnostic.
    if 'public.agaveapi.co' not in agave.api_server:
        return
    local_path = os.path.join(HERE, 'local_test_download_job')
    uri = 'https://public.agaveapi.co/jobs/v2/412474231577973221-242ac113-0001-007/outputs/listings/algebra/sum/data/out.txt'
    agave.download_uri(uri, local_path)
    assert os.path.exists(local_path)
    os.remove(local_path)

def test_download_job_output_media_uri(agave):
    # this test currently does not work on other tenants.
    # todo - update to make tenant-agnostic.
    if 'public.agaveapi.co' not in agave.api_server:
        return
    local_path = os.path.join(HERE, 'local_test_download_job')

    uri = 'https://public.agaveapi.co/jobs/v2/412474231577973221-242ac113-0001-007/outputs/media/algebra/sum/data/out.txt'
    agave.download_uri(uri, local_path)
    assert os.path.exists(local_path)
    os.remove(local_path)

def test_list_uploaded_file(agave, credentials):
    files = agave.files.list(filePath=credentials['storage_user'], systemId=credentials['storage'])
    for f in files:
        if 'test_file_upload_python_sdk' in f.path:
            break
    else:
        assert False

def test_list_uploaded_binary_file(agave, credentials):
    files = agave.files.list(filePath=credentials['storage_user'], systemId=credentials['storage'])
    for f in files:
        if 'test_upload_python_sdk_g_art.mov' in f.path:
            break
    else:
        assert False

def test_delete_uploaded_files(agave, credentials):
    uploaded_files = ['test_file_upload_python_sdk', 'test_upload_python_sdk_g_art.mov']
    for f in uploaded_files:
        agave.files.delete(systemId=credentials['storage'],
                           filePath='{}/{}'.format(credentials['storage_user'], f))
        # make sure file isn't still there:
        files = agave.files.list(filePath=credentials['storage_user'], systemId=credentials['storage'])
        assert f not in [fl.path for fl in files]

def test_submit_job(agave, test_job):
    job = agave.jobs.submit(body=test_job)
    validate_job(job)
    # create an async object
    arsp = AgaveAsyncResponse(agave, job)
    # block until job finishes with a timeout of 3 minutes.
    assert arsp.result(180) == 'FINISHED'

def test_list_jobs(agave):
    jobs = agave.jobs.list()
    for job in jobs:
        validate_job(job)

def test_list_jobs_multiple(agave):
    for i in range(1, 15):
        jobs = agave.jobs.list()
        for job in jobs:
            validate_job(job)

def test_list_single_job_many_times(agave):
    jobs = agave.jobs.list()
    job = jobs[0]
    for i in range(1, 15):
        agave.jobs.get(jobId=job.id)

def test_search_jobs(agave):
    # get the id of the first job from the full list
    id = agave.jobs.list()[0].id
    # use the search to filter for it:
    jobs = agave.jobs.list(search={'id.like': id})
    assert len(jobs) == 1

def validate_pem(pem):
    assert pem.username
    assert pem.permission

def test_list_job_permissions(agave):
    job = agave.jobs.list()[0]
    pems = agave.jobs.listPermissions(jobId=job.id)
    for pem in pems:
        validate_pem(pem)

def test_submit_archive_job(agave, test_job, credentials):
    test_job['archive'] = True
    test_job['archiveSystem'] = credentials['storage']
    job = agave.jobs.submit(body=test_job)
    validate_job(job)
    # create an async object
    arsp = AgaveAsyncResponse(agave, job)
    # block until job finishes with a timeout of 3 minutes.
    assert arsp.result(180) == 'FINISHED'
    # now check that the result was archived


def test_geturl(agave):
    job = agave.jobs.list()[0]
    url = job._links['self']['href']
    job_rsp = agave.geturl(url)
    assert job_rsp.json().get('result').get('id') is not None

def test_get_profile(agave, credentials):
    prof = agave.profiles.get()
    if credentials.get('username'):
        validate_profile(prof, credentials['username'])

def test_list_profiles(agave, credentials):
    prof = agave.profiles.listByUsername(username='me')
    if credentials.get('username'):
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

def validate_role(role):
    assert role.username
    assert role.role

def test_list_system_roles(agave, credentials):
    roles = agave.systems.listRoles(systemId=credentials['storage'])
    for role in roles:
        validate_role(role)

def test_get_system_role_for_user(agave, credentials):
    role = agave.systems.getRoleForUser(systemId=credentials['storage'], username=credentials['username'])
    validate_role(role)

def test_list_metadata(agave):
    md = agave.meta.listMetadata()
    # there may not be any meta data in the system, so simply ensure the response code is a 20x.

def test_list_metadata_with_query_empty(agave):
    md = agave.meta.listMetadata(q = "{'name': 'foofymcfoofoo'}")
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
    assert uuid not in [md.uuid for md in mds]

def test_metadata_admin_pems(agave, credentials):
    # first, lets add a new metadata using the normal user's client
    name = 'python-sdk-test-metadata-admin-pems'
    value = 'test value'
    d = {'name': name,
         'value': value}
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

def validate_postit(postit):
    assert postit.url
    assert postit.method

def test_create_postit(agave, credentials):
    body = {'url':'{}/systems/v2'.format(credentials['apiserver']),
            'maxUses': 2,
            'noauth': False,
            'method': 'GET'
    }
    agave.postits.create(body=body)


def test_list_postits(agave):
    postits = agave.postits.list()
    for postit in postits:
        validate_postit(postit)

def validate_notification(n):
    assert n.id
    assert n.event
    assert n.url

# def test_create_notification_to_email(agave, credentials):
# todo - replace with a "fake email"
#     # get uuid of storage system
#     stor = agave.systems.get(systemId=credentials['storage'])
#     assert stor.uuid
#     body = {"associatedUuid": stor.uuid,
#             "event": "*",
#             "persistent": True,
#             "url": "jstubbs@tacc.utexas.edu"
#     }
#     n = agave.notifications.add(body=json.dumps(body))
#     validate_notification(n)
#     # make sure it's there
#     ns = agave.notifications.list(associatedUuid=stor.uuid)
#     for nt in ns:
#         if nt.id == n.id:
#             break
#     else:
#         assert False

def test_create_notification_to_url(agave, credentials, test_storage_system):
    # first, create a request bin
    base_url = 'https://requestb.in/api/v1/bins'
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


def test_list_notification(agave, credentials):
    # get uuid of storage system
    stor = agave.systems.get(systemId=credentials['storage'])
    assert stor.uuid
    ns = agave.notifications.list(associatedUuid=stor.uuid)
    for n in ns:
        validate_notification(n)


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
    base_url = 'https://requestb.in/api/v1/bins'
    rsp = requests.post(base_url)
    bin_name = rsp.json().get('name')
    bin_url = '{}/{}'.format(base_url, bin_name)
    notification_target = 'https://requestb.in/{}'.format(bin_name)
    # create notification
     # get uuid of storage system
    stor = agave.systems.get(systemId=credentials['storage'])
    assert stor.uuid
    body = {"associatedUuid": stor.uuid,
            "event": "*",
            "persistent": True,
            "url": notification_target
    }
    n = agave.notifications.add(body=json.dumps(body))
    # wait for notification to be propagated
    time.sleep(3)
    # update the system:
    agave.systems.add(body=test_storage_system)
    # wait for notification to be sent
    time.sleep(18)
    # check for a notification
    rsp = requests.get('{}/requests'.format(bin_url))
    assert len(rsp.json()) > 0
    # delete the notification
    agave.notifications.delete(uuid=n.id)

token_callback_calls = 0

def test_token_callback(agave, credentials):

    def sample_token_callback(**kwargs):
        global token_callback_calls
        token_callback_calls += 1
        assert kwargs['access_token']
        assert kwargs['refresh_token']
        assert kwargs['created_at']
        assert kwargs['expires_at']

    # create a client with a token callback:
    ag = a.Agave(username=credentials.get('username'),
                  password=credentials.get('password'),
                  api_server=credentials.get('apiserver'),
                  api_key=credentials.get('apikey'),
                  api_secret=credentials.get('apisecret'),
                  verify=credentials.get('verify_certs', True),
                  token_callback=sample_token_callback)
    # once created, let's force a refresh
    ag.token.refresh()
    global token_callback_calls
    assert token_callback_calls >= 1


def test_token_access(credentials):
    # create a fresh client
    ag = a.Agave(username=credentials.get('username'),
                 password=credentials.get('password'),
                 api_server=credentials.get('apiserver'),
                 api_key=credentials.get('apikey'),
                 api_secret=credentials.get('apisecret'),
                 token=credentials.get('token'),
                 refresh_token=credentials.get('refresh_token'),
                 verify=credentials.get('verify_certs', True))
    # force a token refresh
    token = ag.token.refresh()
    # now, create a new client using just the token
    token_client = a.Agave(api_server=credentials['apiserver'],
                           token=token,
                           verify=credentials.get('verify_certs', True))
    # make sure the new client works
    apps = token_client.apps.list()
    for app in apps:
        validate_app(app)