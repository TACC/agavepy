"""
    files_tests.py
"""
import pytest
import cgi
import filecmp
import json
import mimetypes
import os
import shutil
import tempfile
import time
from testsuite_utils import MockServer                                          
from response_templates import response_template_to_json

try: # python 2
    from BaseHTTPServer import BaseHTTPRequestHandler
except ImportError: # python 3
    from http.server import BaseHTTPRequestHandler
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from agavepy.agave import Agave



class MockServerFilesEndpoints(BaseHTTPRequestHandler):
    def send_headers(self):
        # The path corresponds to the service being queried. For example,
        # querying "http://localhost:80/f/file.txt" will set the path as
        # "/f/file.txt". 
        npath = os.path.normpath(self.path)
        npath = npath[1:]
        path_elements = npath.split("/")

        # Check access token.
        try: # Python 2
            valid_access_token = self.headers.getheader("Authorization")
        except AttributeError: # Python 3
            valid_access_token = self.headers.get("Authorization")
        if not valid_access_token:
            self.send_error(401, "Unauthorized")
            return None

        # Send headers for /files/v2/media/system requests.
        if "/files/v2/media/system" in self.path: 
            self.send_response(200)
            self.send_header("Content-Type", "text/json; character=utf-8")
            self.end_headers()
        else:
            self.send_error(404, "fuck")
            return None
    
        return path_elements


    def do_GET(self):
        """ Get a file

        This route responds with the contents of a file. The file is expected
        to be in the current working directory and is expected to be created by
        the test setup.
        """
        # elements is a list of path elements, i.e., "/a/b" == ["a", "b"].
        elements = self.send_headers()
        if elements is None or not "/files/v2/media/system" in self.path:
            return

        # Send contents of file to wfile object.
        filename = elements[-1]
        if "?pretty=true" in filename: filename = filename[:-len("?pretty=true")]
        with open(filename, "rb") as f:
            shutil.copyfileobj(f, self.wfile)





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
        MockServer.serve.__func__(cls, MockServerFilesEndpoints)

    def create_local_dummy_file(self):
        """ Create a dummy file for testing

        Create a dummy file to test file copying with the cli. Emulate a file
        on a local system.
        """
        _, file_path = tempfile.mkstemp()
        try:
            with open(file_path, "w") as tmp:
                tmp.write("this is a test file\n")
        except:
            os.remove(file_path)

        return file_path

    def create_remote_dummy_file(self):
        """ Create a dummy file for testing

        Create a dummy file to test file copying with the cli. Emulate a file
        on a remote agave system.
        """
        tmp_filename = "thisisatest.txt"
        with open(tmp_filename, "w") as tmp:
            tmp.write("this emulates a file on a remote system\n")
        return tmp_filename

    def test_files_download(self):
        """ Test file copying from a remote to the local system
        """
        # Create a "remote" dummy file.
        tmp_file = self.create_remote_dummy_file()

        # Destination of downloaded file.
        local_file = "testfile.txt"

        try:
            local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
            agave = Agave(api_server=local_uri)
            agave.token = "mock-access-token"

            agave.files_download("tacc-globalfs-user/"+tmp_file, local_file)
        finally:
            assert filecmp.cmp(tmp_file, local_file)

            # rm dummy file in current working directory.
            if os.path.exists(tmp_file):
                os.remove(tmp_file)
