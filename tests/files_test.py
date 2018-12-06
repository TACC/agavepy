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

from agavepy.agave import Agave


# Sample successful responses from the agave api.
sample_files_upload_response = response_template_to_json("files-upload.json")


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
            self.send_response(400)
            self.end_headers()
            return

        # Send contents of file to wfile object.
        filename = elements[-1]
        if "?pretty=true" in filename: filename = filename[:-len("?pretty=true")]
        with open(filename, "rb") as f:
            shutil.copyfileobj(f, self.wfile)


    def do_POST(self):
        """ Upload or import a file

        Save uploaded file to current working directory and send a response.
        """
        # elements is a list of path elements, i.e., ["a", "b"] ~ "/a/b".
        elements = self.send_headers()
        if elements is None or not "/files/v2/media/system" in self.path:
            self.send_response(400)
            self.end_headers()
            return

        # Submitted form data.
        form = cgi.FieldStorage(
            fp = self.rfile,
            headers = self.headers,
            environ = {
                "REQUEST_METHOD": "POST",
                "CONTENT_TYPE": self.headers["Content-Type"]
            })

        # Check if request is for uploading or importing a file.
        action = ""
        if form.getvalue("fileToUpload", "") != "":
            action = "upload"
        elif form.getvalue("urlToIngest", "") != "":
            action = "import"
        else:
            self.send_response(400)
            self.end_headers()
            return

        if action == "upload":
            # Save uploaded file.
            fname = form["fileToUpload"].filename
            with open(fname, "wb") as flocal:
                shutil.copyfileobj(form["fileToUpload"].file, flocal)
                
            # Send response.
            request_source = self.headers.get("HOST")
            file_path      = "/".join(elements[5:] + [fname])
            system_id      = elements[4]
            request_url    = "".join(["https://tenant", self.path, "/", fname])
            system_url     = "".join(["https://tenant", "/systems/v2/", system_id])
            history_url    = "".join(["https://tenant", "/files/v2/history/system/", system_id, "/", file_path])
            sample_files_upload_response["result"]["name"] = fname
            sample_files_upload_response["result"]["source"] = request_source
            sample_files_upload_response["result"]["path"] = file_path
            sample_files_upload_response["result"]["systemId"] = system_id
            sample_files_upload_response["result"]["_links"]["self"]["href"] = request_url
            sample_files_upload_response["result"]["_links"]["system"]["href"] = system_url
            sample_files_upload_response["result"]["_links"]["history"]["href"] = history_url
            
            try: # python 2
                self.wfile.write(json.dumps(sample_files_upload_response))
            except TypeError:
                self.wfile.write(json.dumps(sample_files_upload_response).encode())
        
        elif action == "import":
            self.send_response(200)
            self.end_headers()
            return


    def do_PUT(self):
        """ Mock endpoint to test files_copy and files_move method.
        """
        # elements is a list of path elements, i.e., ["a", "b"] ~ "/a/b".
        elements = self.send_headers()
        if elements is None or not "/files/v2/media/system" in self.path:
            self.send_response(400)
            self.end_headers()
            return

        # Submitted form data.
        form = cgi.FieldStorage(
            fp = self.rfile,
            headers = self.headers,
            environ = {
                "REQUEST_METHOD": "PUT",
                "CONTENT_TYPE": self.headers["Content-Type"]
            })

        # Check access token is not empty.
        token = self.headers.getheader("Authorization")
        if token is None or token == "":
            self.send_response(400)
            self.end_headers()
            return

        # Check request data.
        if form.getvalue("action", "") == "":
            self.send_response(400)
            self.end_headers()
            return

        if form.getvalue("path", "") == "":
            self.send_response(400)
            self.end_headers()
            return


    def do_DELETE(self):                                                          
        """ Delete file                                                         
        """                                                                     
        # elements is a list of path elements, i.e., ["a", "b"] ~ "/a/b".       
        elements = self.send_headers()                                          
        if elements is None or not "/files/v2/media/system" in self.path:       
            return

        # Delete file or directory.
        filename = elements[-1]
        if "?pretty=true" in filename: filename = filename[:-len("?pretty=true")]
        if os.path.isdir(filename):
            # Delete directory.
            shutil.rmtree(filename)
            return
        elif os.path.isfile(filename):
            # Delete file.
            os.remove(filename)
            return
        else:
            self.send_response(400)
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
            agave.created_at = str(int(time.time()))
            agave.expires_in = str(14400)

            agave.files_download("tacc-globalfs-user/"+tmp_file, local_file)
        finally:
            assert filecmp.cmp(tmp_file, local_file)

            # rm local file.
            if os.path.exists(local_file):
                os.remove(local_file)
            # rm dummy file in current working directory.
            if os.path.exists(tmp_file):
                os.remove(tmp_file)


    def test_files_upload(self):
        """ Test file uload to remote systems
        """
        # Create a local dummy file.
        tmp_file = self.create_local_dummy_file()

        try:
            local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
            agave = Agave(api_server=local_uri)
            agave.token = "mock-access-token"
            agave.created_at = str(int(time.time()))
            agave.expires_in = str(14400)

            agave.files_upload(tmp_file, "tacc-globalfs-user/")
        finally:
            _, tmp_filename = os.path.split(tmp_file)
            assert filecmp.cmp(tmp_file, tmp_filename)

            # rm dummy file.
            os.remove(tmp_file)
            # rm dummy file in current working directory.
            if os.path.exists(tmp_filename):
                os.remove(tmp_filename)

    def test_files_delete(self):
        """ Test file copying from a remote to the local system
        """
        # Create a "remote" dummy file.
        tmp_file = self.create_remote_dummy_file()

        try:
            local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
            agave = Agave(api_server=local_uri)
            agave.token = "mock-access-token"
            agave.created_at = str(int(time.time()))
            agave.expires_in = str(14400)

            agave.files_delete("tacc-globalfs-user/"+tmp_file)
        finally:
            assert os.path.exists(tmp_file) == False


            # rm dummy file in current working directory.
            if os.path.exists(tmp_file):
                os.remove(tmp_file)

    def test_files_copy(self):
        """ test files copying from remote to remote

        The call to files_copy has no side effects on the host so the function
        call should simply be able to return successfully.
        """
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        agave = Agave(api_server=local_uri)
        agave.token = "mock-access-token"
        agave.created_at = str(int(time.time()))
        agave.expires_in = str(14400)
        
        agave.files_copy("tacc-globalfs/file", "tacc-globalfs/file-copy")


    def test_files_move(self):
        """ test files move method

        The call to files_move has no side effects on the host so the function
        call should simply be able to return successfully.
        """
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        agave = Agave(api_server=local_uri)
        agave.token = "mock-access-token"
        agave.created_at = str(int(time.time()))
        agave.expires_in = str(14400)

        agave.files_copy("tacc-globalfs/file", "tacc-globalfs/another-file")


    def test_files_mkdir(self):
        """ test files mkdir method

        The call to files_mkdir has no side effects on the host so the function
        call should simply be able to return successfully.
        """
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        agave = Agave(api_server=local_uri)
        agave.token = "mock-access-token"
        agave.created_at = str(int(time.time()))
        agave.expires_in = str(14400)

        agave.files_mkdir("tacc-globalfs/new/path")


    def test_files_import(self, capfd):
        """ Test files import
        """
        local_uri = "http://localhost:{port}/".format(port=self.mock_server_port)
        agave = Agave(api_server=local_uri)
        agave.token = "mock-access-token"
        agave.created_at = str(int(time.time()))
        agave.expires_in = str(14400)

        # Import file.
        agave.files_import("agave://data-sd2e-community/test.txt", "tacc-globalfs-username/")
        out, err = capfd.readouterr()
        assert "200" in err
