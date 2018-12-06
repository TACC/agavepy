"""
    files-listings_tests.py
"""
import pytest
import json
import os
import sys
from testsuite_utils import MockServer
from response_templates import response_template_to_json
try: # python 2                                                                 
    from BaseHTTPServer import BaseHTTPRequestHandler                           
except ImportError: # python 3                                                  
    from http.server import BaseHTTPRequestHandler
from agavepy.agave import Agave


# Sample successful responses from the agave api.
sample_files_list_response = response_template_to_json("files-list.json")



class MockServerListingsEndpoints(BaseHTTPRequestHandler):
    """ Mock the Agave API
    """
    def do_GET(self):
        """ Mock oauth client listing.
        """
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(sample_files_list_response).encode())



class TestMockServer(MockServer):
    """ Test file listing-related agave api endpoints 
    """

    @classmethod
    def setup_class(cls):
        """ Set up an agave mock server

        Listen and serve mock api as a daemon.
        """
        MockServer.serve.__func__(cls, MockServerListingsEndpoints)


    def test_files_list(self, capfd):
        """ Test files listings
        """
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        agave = Agave(api_server=local_uri)
        agave.token = "mock-access-token"

        # List files.
        agave.files_list("tacc-globalfs-username/tests", long_format=False)

        # Stdout should contain the putput from the command.
        # Stderr will contain logs from the mock http server.
        out, err = capfd.readouterr()
        assert "copy.txt" in out
        assert "sp1-copy.fq" in out
        assert "upload.txt" in out
        assert "\"GET //files/v2/listings/system/tacc-globalfs-username/tests?pretty=true HTTP/1.1\" 200" in err 
