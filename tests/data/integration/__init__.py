__author__ = 'jstubbs'

import json
import os

import agavepy.agave as a

HERE = os.path.abspath(__file__)
PARENT = os.path.dirname(HERE)

__all__ = [
    'MockData', 'TEST_UPLOAD_FILE', 'TEST_UPLOAD_BINARY_FILE',
    'TEST_UPLOAD_TIMEOUT'
]

TEST_UPLOAD_FILE = os.path.join(PARENT, 'test_file_upload_python_sdk')
TEST_UPLOAD_BINARY_FILE = os.path.join(PARENT,
                                       'test_upload_python_sdk_g_art.mov')
TEST_UPLOAD_TIMEOUT = 360


class MockData(object):
    def __init__(self, credentials):
        self.local_data = credentials

    def file_to_json(self, filename):
        return json.load(open(os.path.join(PARENT, filename)))

    def get_test_storage_system(self,
                                id=None,
                                host=None,
                                user=None,
                                pubkey=None,
                                privkey=None):
        """
        Example storage system read from an external file.
        """
        storage = self.file_to_json('test-storage.json')
        if id is not None:
            storage['id'] = id

        if host is not None:
            storage['storage']['host'] = host

        if user is not None:
            storage['storage']['auth']['username'] = user

        if pubkey is not None:
            storage['storage']['auth']['publicKey'] = pubkey

        if privkey is not None:
            storage['storage']['auth']['privateKey'] = privkey

        return storage

    def get_test_compute_system(self,
                                id=None,
                                host=None,
                                user=None,
                                pubkey=None,
                                privkey=None):
        """
        Example compute system defined inline.
        """
        compute = self.file_to_json('test-compute.json')
        if id is not None:
            compute['id'] = id

        if host is not None:
            compute['login']['host'] = host
            compute['storage']['host'] = host

        if user is not None:
            compute['login']['auth']['username'] = user
            compute['storage']['auth']['username'] = user

        if pubkey is not None:
            compute['login']['auth']['publicKey'] = pubkey
            compute['storage']['auth']['publicKey'] = pubkey

        if privkey is not None:
            compute['login']['auth']['privateKey'] = privkey
            compute['storage']['auth']['privateKey'] = privkey

        return compute

    def get_test_app_from_file(self):
        app = self.file_to_json('test-app.json')
        app['name'] = self.local_data['app_name']
        app['executionSystem'] = self.local_data['execution']
        app['deploymentSystem'] = self.local_data['storage']
        return app

    def get_test_job_from_file(self):
        """
        Example job request read in from an external file.
        """
        test_app = self.get_test_app_from_file()
        test_stor = self.get_test_storage_system()
        job = self.file_to_json('test-job.json')
        job['appId'] = test_app['name'] + '-' + test_app['version']
        job['inputs']['wf'] = "agave://{}//data/algebra.yml".format(
            test_stor['id'])
        return job
