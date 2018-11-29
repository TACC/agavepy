"""
    files-pems_tests.py
"""
import pytest
import json
import os
import sys
import time
from testsuite_utils import MockServer
from response_templates import response_template_to_json
try: # python 2                                                                 
    from BaseHTTPServer import BaseHTTPRequestHandler                           
except ImportError: # python 3                                                  
    from http.server import BaseHTTPRequestHandler
from agavepy.agave import Agave


# Sample successful responses from the agave api.
sample_files_pems_list_response = response_template_to_json("files-pems-list.json")



class MockServerListingsEndpoints(BaseHTTPRequestHandler):
    """ Mock the Agave API
    """
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(sample_files_pems_list_response).encode())



class TestMockServer(MockServer):
    """ Test file listing-related agave api endpoints 
    """

    @classmethod
    def setup_class(cls):
        """ Set up an agave mock server

        Listen and serve mock api as a daemon.
        """
        MockServer.serve.__func__(cls, MockServerListingsEndpoints)


    def test_files_pems_list(self, capfd):
        """ Test files listings
        """
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        agave = Agave(api_server=local_uri)
        agave.token = "mock-access-token"
        agave.created_at = str(int(time.time()))
        agave.expires_in = str(14400)

        # List files.
        agave.files_pems_list("tacc-globalfs-username/")

        # Stdout should contain the putput from the command.
        # Stderr will contain logs from the mock http server.
        out, err = capfd.readouterr()
        assert "username" in out
        assert "yes" in out
        assert "200" in err 
