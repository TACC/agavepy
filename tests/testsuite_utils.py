"""
    testsuite_utils.py

Methods used throughout the test suite for testing.
"""
import socket
from threading import Thread
try: # python 2
    from BaseHTTPServer import HTTPServer
except ImportError: # python 3
    from http.server import HTTPServer



def get_free_port():
    """ Find a free port

    Return a port available for connecting on localhost.
    """
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(("localhost", 0))
    addr, port = s.getsockname()
    s.close()
    return port


class MockServer(object):
    """ Mock server

    Run an HTTP server as a daemon in a thread.
    """

    @classmethod
    def serve(cls, http_server):
        """ Set up mock server

        INPUTS
        -------
        http_server: BaseHTTPRequestHandler
            HTTP server with request handlers specified
        """
        # Find a port to listen to connect.
        cls.mock_server_port = get_free_port()
        # Instantiate server.
        cls.mock_server = \
                HTTPServer(("localhost", cls.mock_server_port), http_server)

        cls.mock_server_thread = Thread(target=cls.mock_server.serve_forever)
        cls.mock_server_thread.setDaemon(True)
        cls.mock_server_thread.start()
