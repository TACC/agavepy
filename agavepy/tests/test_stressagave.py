# Additional tests that are either long running (such as large file uploads) or otherwise stress the Agave system.
# These tests do not necessarily need to be run as part of the development cycle but should be run as part of a release.
#
# To run the tests:
# 1. create a file, test_credentials.json, in the tests directory with credentials for accessing a tenant (see the ex).
#    Make sure to update: storage, storage_key, execution and execution_key and app_name
#
# 2. update the test-storage.json, test-compute.json, test-app.json and test-job.json
#
# 3. To run the tests, use the following from the tests directory with the requrements.txt installed (or activate a
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
import testdata

HERE = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope='session')
def credentials():
    credentials_file = os.environ.get('creds', 'test_credentials.json')
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


def test_upload_large_file(agave, credentials):
    rsp = agave.files.importData(systemId=credentials['storage'],
                                 filePath=credentials['storage_user'],
                                 fileToUpload=open('test_largefile_upload_python_sdk', 'rb'))
    arsp = AgaveAsyncResponse(agave, rsp)
    status = arsp.result(timeout=120)
    assert status == 'FINISHED'

