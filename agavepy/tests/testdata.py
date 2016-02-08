__author__ = 'jstubbs'

import json
import os

import agavepy.agave as a

HERE = os.path.dirname(os.path.abspath(__file__))

class TestData(object):

    def __init__(self, credentials):
        self.local_data = credentials

    def file_to_json(self, filename):
        return json.load(open(os.path.join(HERE, filename)))

    def get_test_storage_system(self):
        """
        Example storage system read from an external file.
        """
        storage = self.file_to_json('test-storage.json')
        storage['id'] = self.local_data['storage']
        storage['storage']['auth']['privateKey'] = self.local_data['storage_key']
        return storage

    def get_test_compute_system(self):
        """
        Example compute system defined inline.
        """
        compute = self.file_to_json('test-compute.json')
        compute['id'] = self.local_data['execution']
        compute['login']['auth']['privateKey'] = self.local_data['execution_key']
        compute['storage']['auth']['privateKey'] = self.local_data['storage_key']
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
        job['inputs']['wf'] = "agave://{}//data/algebra.yml".format(test_stor['id'])
        return job
