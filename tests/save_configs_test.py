"""
    save_configs_test.py

Test save configuration function.    
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
            a.client_name = "client-1"
            a.username = "user-1"
            a.save_configs(cache_dir)

            b = Agave(tenant_id="tacc.prod")
            b.client_name = "client-2"
            b.username = "user-2"
            b.save_configs(cache_dir)

            c = Agave(tenant_id="sd2e")
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
