"""
    tokens_test.py

Test Agavepy.get_access_token() and refresh_tokens() methods.
"""
import pytest
import cgi
import json                                                                     
import os
import sys
import time
from http.server import BaseHTTPRequestHandler
from testsuite_utils import MockServer
from response_templates import response_template_to_json

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agavepy.agave import Agave


# Agave will provide a response with the following format upon a
# successfull attempt at creating an access token. Refreshing a token results
# in a response with the same format.
sample_token_create_response = response_template_to_json("auth-tokens-create.json")


class MockServerTokenEndpoints(BaseHTTPRequestHandler):
    """ Mock token managament endpoints.
    """

    def do_POST(self):
        """ Test token creation and refreshing
        """
        # Get request data (curl's -d).
        form = cgi.FieldStorage(
            fp = self.rfile,
            headers = self.headers,
            environ={'REQUEST_METHOD': 'POST'})

        # Check that username and password are set. Else, refresh_token should
        # be set.
        username = form.getvalue("username", "")
        password = form.getvalue("password", "")
        refresh_token = form.getvalue("refresh_token", "")

        if form.getvalue("grant_type", "") == "password":
            if username == "" or password == "":
                self.send_response(400)
                self.end_headers()
                return
        elif form.getvalue("grant_type", "") == "refresh_token":
            if refresh_token == "":
                self.send_response(400)
                self.end_headers()
                return
        else:
            self.send_response(400)
            self.end_headers()
            return

        # Check scope is set.
        if form.getvalue("scope", "") != "PRODUCTION":
            self.send_response(400)
            self.end_headers()
            return

        # Update response fields.
        sample_token_create_response["refresh_token"] = "refresh token"
        sample_token_create_response["access_token"] = "access token"

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(sample_token_create_response).encode())



class TestMockServer(MockServer):
    """ Test token-related endpoints.

    Test Agave.get_access_token().
    """

    @classmethod
    def setup_class(cls):
        """ Set up an agave mock server

        Listen and serve mock api as a daemon.
        """
        MockServer.serve.__func__(cls, MockServerTokenEndpoints)


    @patch("agavepy.tokens.create_access_token.getpass.getpass")
    def test_get_access_token(self, mock_pass):
        """ Test access token creation

        Patch username and password from user to send a client create request
        to mock server.
        """
        # Patch password prompt.
        mock_pass.return_value = "pass"

        # Instantiate Agave object making reference to local mock server.
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        ag = Agave(api_server=local_uri, username="user")
        ag.api_key = "somekey"
        ag.api_secret = "somesecret"

        # Get access token.
        ag.get_access_token()

        assert ag.token == "access token"
        assert ag.refresh_token == "refresh token"


    def test_refresh_tokens(self):
        """ Test refresh token operation
        """
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        ag = Agave(api_server=local_uri)
        ag.api_key = "xxx"
        ag.api_secret = "xxx"
        ag.refresh_token = "xxx"
        # See agavepy/agave.py:refresh_tokens() for more info.
        ag.created_at = str( int(time.time()) - 100 )
        ag.expires_in = str(0)

        # Refresh access token
        ag.refresh_tokens()

        assert ag.token == "access token"
        assert ag.refresh_token == "refresh token"
