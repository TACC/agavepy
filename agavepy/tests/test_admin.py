# Additional tests for the admin services.
# These tests should be run for deployments/tenants that are making critical use of the admin services.
#
# To run the tests:
# 0. If wanting to run against the local copy of agavepy, make sure to activate a virtualenv that does
#     not have it installed, and then run out of the project root and preface the test files accordingly,
#     e.g., py.test agavepy/tests/test_admin.py
#
# 1. create a file, test_credentials_admin_tests.json, in the tests directory with credentials for accessing the admin
#    services within a tenant. In particular, you need:
#      - a username (and password) for a user in the <tenant_id>-sandbox-services-admin role.
#      - an OAuth client key (and secret) for a client that has been subscribed to the AdminServices API.
#
# 2. Note that many of the configs needed to run the main agave tests (e.g. storage_key) are not needed
#    by the test_admin.py suite.
#
# 3. To run the tests, use the following from the tests directory with the requrements.txt installed (or activate a
#    virtualenv with the requirements):
#
#    py.test                            -- Run all tests
#    py.test test_admin.py::<test_name> -- Run a single test whose name is <test_name>
#    py.test -k <string>                -- Run all tests with <string> in the name.
#
#    Examples:
#    py.test test_admin.py::test_list_accounts
#    py.test -k accounts


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
    credentials_file = os.environ.get('creds', 'test_credentials_admin_tests.json')
    print "Using: {}".format(credentials_file)
    return json.load(open(
        os.path.join(HERE, credentials_file)))

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


def validate_account_summary(account):
    assert 'id' in account

def validate_account(account):
    assert 'id' in account
    assert 'roles' in account
    roles = account['roles']
    assert 'Internal_everyone'

def validate_role_summary(role):
    assert 'id' in role

def validate_role(role):
    assert 'id' in role
    assert 'accounts' in role

def validate_client(client):
    assert 'id' in client
    assert 'name' in client
    assert 'owner' in client

def validate_api_summary(api):
    assert 'id' in api
    assert 'name' in api
    assert 'owner' in api
    assert 'status' in api
    assert 'version' in api

def validate_api_details(api):
    validate_api_summary(api)
    assert api['id'] == 'Apps-admin-v2'
    assert api['name'] == 'Apps'
    assert api['owner'] == 'admin'
    assert api['status'] == 'PUBLISHED'
    assert api['version'] == 'v2'
    assert api['context'] == '/apps/v2'
    assert 'roles' in api
    assert api['roles'] == ['']
    assert 'visibility' in api
    assert api['visibility'] == 'public'
    assert 'environments' in api
    assert api['environments'] == 'Production and Sandbox'


def test_list_accounts(agave):
    accounts = agave.admin.listAccounts()
    for a in accounts:
        validate_account_summary(a)

def test_add_account(agave):
    body = {'accountId': 'agpytest_suite_svc_account',
            'password': 'QzxJ42917hh$.55'}
    rsp = agave.admin.addAccount(body=body)
    validate_account(rsp)

def test_get_account(agave):
    rsp = agave.admin.getAccount(accountId='agpytest_suite_svc_account')
    validate_account(rsp)

def test_added_account_in_list(agave):
    accounts = agave.admin.listAccounts()
    assert 'agpytest_suite_svc_account' in [a.id for a in accounts]

def test_list_roles(agave):
    roles = agave.admin.listRoles()
    for r in roles:
        validate_role_summary(r)

def test_add_role(agave):
    body = {'roleId': 'Internal_agpytest_suite_svc_role'}
    role = agave.admin.addRole(body=body)
    validate_role(role)

def test_get_role(agave):
    role = agave.admin.getRole(roleId='Internal_agpytest_suite_svc_role')
    validate_role(role)

def test_add_role_to_account(agave):
    body = {'roleId': 'Internal_agpytest_suite_svc_role'}
    account = agave.admin.addRoleToAccount(accountId='agpytest_suite_svc_account', body=body)
    validate_account(account)
    roles = account['roles']
    assert 'Internal_agpytest_suite_svc_role' in roles

def test_remove_role_from_account(agave):
    agave.admin.deleteRoleFromAccount(accountId='agpytest_suite_svc_account', roleId='Internal_agpytest_suite_svc_role')
    # check role not there:
    rsp = agave.admin.getAccount(accountId='agpytest_suite_svc_account')
    roles = rsp['roles']
    assert 'Internal_agpytest_suite_svc_role' not in roles

def test_add_account_to_role(agave):
    account = agave.admin.addAccountToRole(body={'accountId': 'agpytest_suite_svc_account'},
                                           roleId='Internal_agpytest_suite_svc_role')
    roles = agave.admin.getAccount(accountId='agpytest_suite_svc_account').roles
    assert 'Internal_agpytest_suite_svc_role' in roles

def test_remove_account_from_role(agave):
    agave.admin.deleteRoleFromAccount(accountId='agpytest_suite_svc_account',
                                      roleId='Internal_agpytest_suite_svc_role')
    roles = agave.admin.getAccount(accountId='agpytest_suite_svc_account').roles
    assert 'Internal_agpytest_suite_svc_role' not in roles

def test_delete_role(agave):
    agave.admin.deleteRole(roleId='Internal_agpytest_suite_svc_role')
    roles = agave.admin.listRoles()
    assert 'Internal_agpytest_suite_svc_role' not in [r.id for r in roles]

def test_delete_account(agave):
    agave.admin.deleteAccount(accountId='agpytest_suite_svc_account')
    accounts = agave.admin.listAccounts()
    assert 'agpytest_suite_svc_account' not in [a.id for a in accounts]

def test_list_clients(agave):
    clients = agave.admin.listClients()
    for c in clients:
        validate_client(c)

def test_list_apis(agave):
    apis = agave.admin.listApis()
    for api in apis:
        validate_api_summary(api)

def test_get_api(agave):
    api = agave.admin.getApi(apiId='Apps-admin-v2')
    validate_api_details(api)

def test_add_api(agave):
    api_desc = json.load(open(os.path.join(HERE, 'httpbin-basic.json')))
    api = agave.admin.addApi(body=api_desc)
    validate_api_summary(api)
    assert api['id'] == 'httpbin_agavepy-admin-v0.1'
    assert api['name'] == 'httpbin_agavepy'
    assert api['context'] == '/httpbin_agavepy/v0.1'
    assert api['status'] == 'CREATED'
    assert api['owner'] == 'admin'
    assert api['version'] == 'v0.1'
    assert api['visibility'] == 'public'

def test_update_api_status(agave):
    api = agave.admin.updateApiStatus(apiId='httpbin_agavepy-admin-v0.1',
                                      body={'status': 'PUBLISHED'})
    assert api['status'] == 'PUBLISHED'

def test_delete_api(agave):
    agave.admin.deleteApi(apiId='httpbin_agavepy-admin-v0.1')
    apis = agave.admin.listApis()
    assert 'httpbin_agavepy-admin-v0.1' not in [a.id for a in apis]




