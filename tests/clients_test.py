"""
    client_tests.py

Test operations related to the management of Agave oauth clients.    
"""
import pytest
import cgi
import json
import os
import sys
from http.server import BaseHTTPRequestHandler
from testsuite_utils import MockServer
from response_templates import response_template_to_json

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agavepy.agave import Agave


# Sample successful responses from the agave api.
sample_client_create_response = response_template_to_json("clients-create.json")
sample_client_list_response = response_template_to_json("clients-list.json")



class MockServerClientEndpoints(BaseHTTPRequestHandler):
    """ Mock the Agave API

    Mock client managament endpoints from the agave api.
    """
    def do_GET(self):
        """ Mock oauth client listing.
        """
        # Check that basic auth is used.
        authorization = self.headers.get("Authorization")
        if authorization == "" or authorization is None:
            self.send_response(400)
            self.end_headers()
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(sample_client_list_response).encode())


    def do_POST(self):
        """ Mock agave client creation
        """
        # Check that basic auth is used.
        authorization = self.headers.get("Authorization")
        if authorization == "" or authorization is None:
            self.send_response(400)
            self.end_headers()
            return

        # Get request data.
        form = cgi.FieldStorage(
            fp = self.rfile,
            headers = self.headers,
            environ={'REQUEST_METHOD': 'POST'})

        # Check client name is set.
        client_name = form.getvalue("clientName", "")
        if client_name == "":
            self.send_response(400)
            self.end_headers()
            return

        # Check client description is set.
        client_description = form.getvalue("description", "")
        if client_description == "":
            self.send_response(400)
            self.end_headers()
            return

        # CHeck client tier is set.
        if form.getvalue("tier", "") == "":
            self.send_response(400)
            self.end_headers()
            return

        # Update response fields.
        sample_client_create_response["result"]["name"] = client_name
        sample_client_create_response["result"]["description"] = client_description
        sample_client_create_response["result"]["consumerKey"] = "some api key"
        sample_client_create_response["result"]["consumerSecret"] = "some secret"

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(sample_client_create_response).encode())


    def do_DELETE(self):
        """ test clients_delete
        """
        # Check that basic auth is used.
        authorization = self.headers.get("Authorization")
        if authorization == "" or authorization is None:
            self.send_response(400)
            self.end_headers()
            return

        self.send_response(200)
        self.end_headers()



class TestMockServer(MockServer):
    """ Test client-related agave api endpoints 

    Tests client creation (HTTP POST request), removal (HTTP DELETE request), 
    and listing (HTTP GET request).
    """

    @classmethod
    def setup_class(cls):
        """ Set up an agave mock server

        Listen and serve mock api as a daemon.
        """
        MockServer.serve.__func__(cls, MockServerClientEndpoints)


    @patch("agavepy.agave.input")
    @patch("agavepy.clients.create.getpass.getpass")
    def test_client_create(self, mock_input, mock_pass):
        """ Test client create op

        Patch username and password from user to send a client create request 
        to mock server.
        """
        # Patch username and password.
        mock_input.return_value = "user"
        mock_pass.return_value = "pass"

        # Instantiate Agave object making reference to local mock server.
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        ag = Agave(api_server=local_uri)

        # Create client.
        ag.clients_create("client-name", "some description")

        assert ag.api_key == "some api key"
        assert ag.api_secret == "some secret"


    @patch("agavepy.agave.input")                                               
    @patch("agavepy.clients.delete.getpass.getpass")
    def test_client_delete(self, mock_input, mock_pass):
        """ Test clients_delete op

        Patch username and password from user to send a client create request
        to mock server.
        """
        # Patch username and password.
        mock_input.return_value = "user"
        mock_pass.return_value = "pass"

        # Instantiate Agave object making reference to local mock server.
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        ag = Agave(api_server=local_uri)
        ag.client_name = "client-name"
        ag.api_key = "some api key"
        ag.api_secret = "some secret"

        # Create client.
        ag.clients_delete()

        assert ag.api_key == ""
        assert ag.api_secret == ""


    @patch("agavepy.agave.input")
    @patch("agavepy.clients.list.getpass.getpass")
    def test_clients_list(self, mock_input, mock_pass, capfd):
        """ Test clients listing

        Patch username and password from user to send a client create request
        to mock server.
        """
        # Patch username and password.
        mock_input.return_value = "user"
        mock_pass.return_value = "pass"

        # Instantiate Agave object making reference to local mock server.
        local_uri = "http://localhost:{port}".format(port=self.mock_server_port)
        ag = Agave(api_server=local_uri)

        # List clients.
        ag.clients_list()

        # Stdout should contain the putput from the command.
        # Stderr will contain logs from the mock http server.
        out, err = capfd.readouterr()
        assert "DefaultApplication" in out
        assert "\"GET /clients/v2 HTTP/1.1\" 200" in err 
