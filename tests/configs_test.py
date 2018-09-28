"""
    configs_test.py

Test save and load configuration function.    
"""
import pytest
import json
import os
import shutil
import sys
import tempfile
from response_templates import response_template_to_json

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agavepy.agave import Agave


# The agave API will provide a response with the following format upon a
# successfull attempt at listing tenants.
sample_tenants_list_response = response_template_to_json("tenants-list.json")

# Sample configuration file using tenants irec and sd2e (sd2e is in current).
sample_config = response_template_to_json("sample-config.json")


class TestSaveConfigs:
    """ Test client-related agave api endpoints 

    Tests client creation (HTTP POST request), removal (HTTP DELETE request), 
    and listing (HTTP GET request).
    """
    
    @patch("agavepy.tenants.tenants.get_tenants")
    def test_save_configs(self, mock_get_tenants):
        """ Test Agave initialization
        """
        # Patch list_tenants function and input.
        mock_get_tenants.return_value = sample_tenants_list_response


        # Instantiate Agave objects and save configurations to cache dir.
        try:
            # create a tmp dir and use it as a cache dir.
            cache_dir = tempfile.mkdtemp()

            a = Agave(tenant_id="sd2e")
            a.init()
            a.client_name = "client-1"
            a.username = "user-1"
            a.save_configs(cache_dir)

            b = Agave(tenant_id="tacc.prod")
            b.init()
            b.client_name = "client-2"
            b.username = "user-2"
            b.save_configs(cache_dir)

            c = Agave(tenant_id="sd2e")
            c.init()
            c.client_name = "client-3"
            c.username = "user-3"
            c.save_configs(cache_dir)

            with open("{}/config.json".format(cache_dir), "r") as f:
                config = json.load(f)

            print(config)
            print()
            print(sample_config)
            assert config == sample_config 
        finally:
            shutil.rmtree(cache_dir)


    @patch("agavepy.tenants.tenants.get_tenants")
    def test_load_configs(self, mock_get_tenants):
        """ Test load_configs function
        """
        try:
            # create a tmp dir and use it as a cache dir.
            cache_dir = tempfile.mkdtemp()
            # Save sample configurations to cache dir.
            with open("{}/config.json".format(cache_dir), "w") as f:
                json.dump(sample_config, f, indent=4)

            ag = Agave()
            ag.load_configs(cache_dir=cache_dir)

            sample_client = list(sample_config["current"].keys())[0]
            assert ag.client_name == sample_client
            assert ag.tenant_id   == sample_config["current"][sample_client]["tenantid"]
            assert ag.username    == sample_config["current"][sample_client]["username"]

        finally:
            shutil.rmtree(cache_dir)


    @patch("agavepy.tenants.tenants.get_tenants")
    def test_load_configs_specify_session(self, mock_get_tenants):
        """ Test load_configs function

        Load a specific session from a configurations file.
        """
        try:
            # create a tmp dir and use it as a cache dir.
            cache_dir = tempfile.mkdtemp()
            # Save sample configurations to cache dir.
            with open("{}/config.json".format(cache_dir), "w") as f:
                json.dump(sample_config, f, indent=4)

            ag = Agave()
            ag.load_configs(cache_dir=cache_dir, tenant_id="tacc.prod", 
                    username="user-2", client_name="client-2")

            assert ag.client_name == "client-2"
            assert ag.username    == "user-2"
            assert ag.tenant_id   == "tacc.prod"

        finally:
            shutil.rmtree(cache_dir)
