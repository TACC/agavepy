"""
    initialize_agave_test.py

Test initialization of Agave object.    
"""
import pytest
import json
import os
import sys
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


class TestAgaveInitialization:
    """ Test client-related agave api endpoints 

    Tests client creation (HTTP POST request), removal (HTTP DELETE request), 
    and listing (HTTP GET request).
    """
    
    @patch("agavepy.tenants.tenants.get_tenants")
    @patch("agavepy.agave.input")
    def test_Agave_init(self, mock_get_tenants, mock_input):
        """ Test Agave initialization
        """
        # Patch list_tenants function and input.
        mock_input.return_value = sample_tenants_list_response
        mock_get_tenants.return_value = "sd2e"

        # Instantiate Agave object making reference to local mock server.
        ag = Agave()

        assert ag.tenant_id == "sd2e"
        assert ag.api_server == "https://api.sd2e.org"
