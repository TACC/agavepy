__author__ = 'vaughn, jstubbs'

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
                               TEST_UPLOAD_FILE, TEST_UPLOAD_TIMEOUT,
                               TEST_JOB_TIMEOUT)

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
def test_job_static_id():
    """This is a known, previously-submitted job
    """
    return '1784a694-0737-480e-95f2-44f55fb35fb7-007'


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


##############
# Validators #
##############


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


def validate_file_pem(pem):
    assert pem.permission
    assert 'execute' in pem.permission
    assert 'read' in pem.permission
    assert 'write' in pem.permission


def validate_history_rec(rec):
    assert rec.description


def validate_job(job):
    assert job.appId
    if 'endTime' in job:
        assert job.endTime is None or type(job.endTime) is datetime.datetime
    assert job.id
    assert job.name
    assert job.owner
    if 'startTime' in job:
        assert job.startTime is None or type(
            job.startTime) is datetime.datetime
    assert job.status


def validate_job_listing(job):
    assert job.id
    assert job.name
    assert job.status
    assert job.owner


def validate_meta(md, name, value):
    assert md.name == name
    assert md.value == value


def validate_monitor(m):
    assert m.id
    assert m.target
    assert m.frequency


def validate_notification(n):
    assert n.id
    assert n.event
    assert n.url


def validate_pem(pem):
    assert pem.username
    assert pem.permission


def validate_postit(postit):
    assert postit.url
    assert postit.method


def validate_profile(prof, user):
    assert prof.username == user


def validate_role(role):
    assert role.username
    assert role.role


def validate_system(system):
    assert type(system.public) is bool
    assert system.name
    assert system.status
    assert system.type


###############
# Add Systems #
###############


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


@pytest.mark.longrun
def test_upload_file(agave, storage_system_id, test_username):
    rsp = agave.files.importData(systemId=storage_system_id,
                                 filePath=test_username,
                                 fileToUpload=open(TEST_UPLOAD_FILE, 'rb'))
    arsp = AgaveAsyncResponse(agave, rsp)
    status = arsp.result(timeout=TEST_UPLOAD_TIMEOUT)
    assert status == 'FINISHED'


@pytest.mark.longrun
def test_download_file(agave, storage_system_id, test_username):
    rsp = agave.files.download(systemId=storage_system_id,
                               filePath='{0}/{1}'.format(
                                   test_username,
                                   os.path.basename(TEST_UPLOAD_FILE)))
    assert rsp.status_code == 200


@pytest.mark.longrun
def test_download_file_range(agave, storage_system_id, test_username):
    rsp = agave.files.download(
        systemId=storage_system_id,
        filePath='{}/test_file_upload_python_sdk'.format(test_username),
        headers={'range': 'bytes=1-5'})
    assert rsp.status_code == 200


@pytest.mark.longrun
def test_upload_binary_file(agave, storage_system_id, test_username):
    rsp = agave.files.importData(systemId=storage_system_id,
                                 filePath=test_username,
                                 fileToUpload=open(TEST_UPLOAD_BINARY_FILE,
                                                   'rb'))
    arsp = AgaveAsyncResponse(agave, rsp)
    status = arsp.result(timeout=TEST_UPLOAD_TIMEOUT)
    assert status == 'FINISHED'


@pytest.mark.longrun
def test_download_binary_file(agave, storage_system_id, test_username):
    rsp = agave.files.download(systemId=storage_system_id,
                               filePath='{0}/{1}'.format(
                                   test_username,
                                   os.path.basename(TEST_UPLOAD_BINARY_FILE)))
    assert rsp.status_code == 200


@pytest.mark.longrun
def test_download_agave_uri(agave, storage_system_id, test_username):
    remote_path = '{}/test_file_upload_python_sdk'.format(test_username)
    local_path = tempfile.mkstemp()[1]
    uri = 'agave://{}/{}'.format(storage_system_id, remote_path)
    rsp = agave.download_uri(uri, local_path)
    assert os.path.exists(local_path)
    os.remove(local_path)


@pytest.mark.longrun
def test_list_uploaded_file(agave, storage_system_id, test_username):
    files = agave.files.list(filePath='{0}/{1}'.format(
        test_username, os.path.basename(TEST_UPLOAD_FILE)),
                             systemId=storage_system_id)
    for f in files:
        if os.path.basename(TEST_UPLOAD_FILE) in f.path:
            break
    else:
        assert False


@pytest.mark.longrun
def test_list_uploaded_binary_file(agave, storage_system_id, test_username):
    files = agave.files.list(filePath='{0}/{1}'.format(
        test_username, os.path.basename(TEST_UPLOAD_BINARY_FILE)),
                             systemId=storage_system_id)
    for f in files:
        if os.path.basename(TEST_UPLOAD_BINARY_FILE) in f.path:
            break
    else:
        assert False


@pytest.mark.longrun
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
        validate_job_listing(job)
    assert len(jobs) > 0, 'Test user has no listable jobs'


@pytest.mark.longrun
def test_list_single_job_many_times(agave):
    jobs = agave.jobs.list()
    if len(jobs) > 0:
        job = jobs[0]
        for i in range(1, 15):
            j = agave.jobs.get(jobId=job.id)
            validate_job(j)
    else:
        raise IndexError('Test user has no listable jobs')


@pytest.mark.longrun
def test_download_job_output_listings_uri(agave, test_job_static_id):
    # Relies on output of job ${test_job_static_id}
    local_path = tempfile.mkstemp()[1]
    uri = '{0}/jobs/v2/{1}/outputs/listings/wc_out/output.txt'.format(
        agave.api_server, test_job_static_id)
    agave.download_uri(uri, local_path)
    assert os.path.exists(local_path)
    os.remove(local_path)


@pytest.mark.longrun
def test_download_job_output_media_uri(agave, test_job_static_id):
    # Relies on output of job ${test_job_static_id}
    local_path = tempfile.mkstemp()[1]
    uri = '{0}/jobs/v2/{1}/outputs/media/wc_out/output.txt'.format(
        agave.api_server, test_job_static_id)
    agave.download_uri(uri, local_path)
    assert os.path.exists(local_path)
    os.remove(local_path)


@pytest.mark.longrun
def test_submit_job(agave, test_job):
    job = agave.jobs.submit(body=test_job)
    validate_job(job)
    # create an async object
    arsp = AgaveAsyncResponse(agave, job)
    # block until job finishes with a timeout of TEST_JOB_TIMEOUT sec.
    assert arsp.result(TEST_JOB_TIMEOUT) == 'FINISHED'


@pytest.mark.longrun
def test_submit_archive_job(agave, test_job, storage_system_id):
    test_job['archive'] = True
    test_job['archiveSystem'] = storage_system_id
    job = agave.jobs.submit(body=test_job)
    validate_job(job)
    # create an async object
    arsp = AgaveAsyncResponse(agave, job)
    # block until job finishes with a timeout of 3 minutes.
    assert arsp.result(TEST_JOB_TIMEOUT) == 'FINISHED'
    # TODO - check that the result was archived


def test_search_jobs(agave):
    # get the id of the first job from the full list
    id = agave.jobs.list()[0].id
    owner = agave.jobs.list()[0].owner
    # use the search to filter for it:
    jobs = agave.jobs.list(search={'id.like': id})
    assert len(jobs) == 1
    jobs = agave.jobs.list(search={'owner.like': owner})
    assert len(jobs) > 1


def test_list_job_permissions(agave):
    job = agave.jobs.list()[0]
    pems = agave.jobs.listPermissions(jobId=job.id)
    for pem in pems:
        validate_pem(pem)


def test_job_geturl(agave):
    job = agave.jobs.list()[0]
    url = job._links['self']['href']
    job_rsp = agave.geturl(url)
    assert job_rsp.json().get('result').get('id') is not None


############
# Profiles #
############


def test_get_profile(agave, test_username):
    prof = agave.profiles.get()
    if test_username:
        validate_profile(prof, test_username)


def test_list_profiles(agave, test_username):
    prof = agave.profiles.listByUsername(username='me')
    if test_username:
        validate_profile(prof, test_username)


###########
# Systems #
###########


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


def test_list_system_roles(agave, storage_system_id, test_username):
    roles = agave.systems.listRoles(systemId=storage_system_id)
    for role in roles:
        validate_role(role)


def test_get_system_role_for_user(agave, storage_system_id, test_username):
    role = agave.systems.getRoleForUser(systemId=storage_system_id,
                                        username=test_username)
    validate_role(role)


#################
# Notifications #
#################


@pytest.fixture(scope='session')
def test_postbin_url():
    base_url = 'https://postb.in'
    api_url = base_url + '/api/bin'
    rsp = requests.post(api_url)
    bin_name = rsp.json().get('binId')
    bin_url = '{}/{}'.format(base_url, bin_name)
    return bin_url


def get_postbin_requests(postbin_url):
    """Return all requests for a postb.in
    """
    pels = postbin_url.split('/')
    requests_url = '{0}//{1}/api/bin/{2}/req/shift'.format(
        pels[0], pels[2], pels[3])
    reqs = []
    count_resp = 0
    while True and count_resp < 100:
        resp = requests.get(requests_url)
        count_resp = count_resp + 1
        if resp.status_code == 200:
            reqs.append(resp.json())
        else:
            return reqs


def test_postbin_url_ok(test_postbin_url):
    assert 'https' in test_postbin_url


def test_create_notification_to_url(agave, storage_system_id,
                                    test_postbin_url):

    # get uuid of storage system
    stor = agave.systems.get(systemId=storage_system_id)
    assert stor.uuid

    body = {
        'associatedUuid': stor.uuid,
        'event': '*',
        'persistent': True,
        'url': test_postbin_url
    }
    n = agave.notifications.add(body=json.dumps(body))


def test_list_notification(agave, storage_system_id):
    # get uuid of storage system
    stor = agave.systems.get(systemId=storage_system_id)
    assert stor.uuid
    ns = agave.notifications.list(associatedUuid=stor.uuid)
    for n in ns:
        validate_notification(n)


@pytest.mark.longrun
def test_notification_to_url(agave, test_postbin_url, test_storage_system):
    # create notification
    # get uuid of storage system
    stor = agave.systems.get(systemId=test_storage_system['id'])
    assert stor.uuid
    body = {
        'associatedUuid': stor.uuid,
        'event': '*',
        'persistent': True,
        'url': test_postbin_url
    }
    n = agave.notifications.add(body=json.dumps(body))
    # wait for notification to be propagated
    time.sleep(6)
    # update the system:
    agave.systems.add(body=test_storage_system)
    # wait for notification to be sent
    time.sleep(24)
    # check for a notification
    reqs = get_postbin_requests(test_postbin_url)
    assert len(reqs) > 0
    # delete the notification
    agave.notifications.delete(uuid=n.id)


def test_delete_notification(agave, storage_system_id):
    # get uuid of storage system
    stor = agave.systems.get(systemId=storage_system_id)
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


def test_create_notification_to_email(agave, storage_system_id):
    # get uuid of storage system
    stor = agave.systems.get(systemId=storage_system_id)
    assert stor.uuid
    body = {
        'associatedUuid': stor.uuid,
        'event': '*',
        'persistent': True,
        'url': 'noreply@tacc.utexas.edu'
    }
    n = agave.notifications.add(body=json.dumps(body))
    validate_notification(n)
    # make sure it's there
    ns = agave.notifications.list(associatedUuid=stor.uuid)
    for nt in ns:
        if nt.id == n.id:
            agave.notifications.delete(uuid=n.id)
            break
    else:
        assert False


############
# Metadata #
############


def test_list_metadata(agave):
    md = agave.meta.listMetadata()
    # there may not be any meta data in the system, so simply ensure the response code is a 20x.


def test_list_metadata_with_query_empty(agave):
    md = agave.meta.listMetadata(q="{'name': 'foofymcfoofoo'}")
    assert len(md) == 0


def test_add_list_delete_metadata(agave):
    # add a new one
    name = 'python-sdk-test-metadata'
    value = 'test value'
    d = {'name': name, 'value': value}
    md = agave.meta.addMetadata(body=json.dumps(d))
    validate_meta(md, name, value)
    # find it in the list:
    mds = agave.meta.listMetadata(q='')
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
    mds = agave.meta.listMetadata(q='')
    assert uuid not in [md.uuid for md in mds]


# TODO - Add a test for searching metdata

###########
# Postits #
###########


def test_create_postit(agave, credentials):
    body = {
        'url': '{}/systems/v2'.format(credentials['apiserver']),
        'maxUses': 2,
        'noauth': False,
        'method': 'GET'
    }
    agave.postits.create(body=body)


def test_list_postits(agave):
    postits = agave.postits.list()
    for postit in postits:
        validate_postit(postit)


#####################
# Token-only Access #
#####################


def test_token_only_access(credentials):
    # create a fresh client
    ag = a.Agave(
        username=credentials.get('username'),
        password=credentials.get('password'),
        api_server=credentials.get('apiserver'),
        api_key=credentials.get('apikey'),
        api_secret=credentials.get('apisecret'),
        #  token=credentials.get('token'),
        #  refresh_token=credentials.get('refresh_token'),
        verify=credentials.get('verify_certs', True))
    # force a token refresh
    token = ag.token.refresh()
    # now, create a new client using just the token
    token_client = a.Agave(api_server=credentials['apiserver'],
                           token=token,
                           verify=credentials.get('verify_certs', True))
    # make sure configured and newly-generated token are not same
    assert credentials.get('token') != token_client._token
    # make sure the new client works
    apps = token_client.apps.list()
    for app in apps:
        validate_app(app)


##################
# Token Callback #
##################

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
    ag.refresh()
    global token_callback_calls
    assert token_callback_calls >= 1
