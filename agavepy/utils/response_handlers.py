"""
    response_hanlders.py
"""
from __future__ import print_function
import sys



class AgaveAPICallError(Exception):
    """ Handle bad responses from Agave
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


def handle_bad_response_status_code(r):                                         
    """ Handle a response with a bad status code                                
    """
    if not r.ok:
        error_msg = "Bad {0} request to {1}, status code {2}\n".format(
            r.request.method, r.url, r.status_code)
        error_msg += "{}\n".format(r.request.body)
        error_msg += "{}\n".format(r.json())

        raise AgaveAPICallError(error_msg)
