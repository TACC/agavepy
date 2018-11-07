"""
    clients.py
"""
import getpass
import requests
from .exceptions import AgaveClientError
from ..utils import handle_bad_response_status_code



def clients_delete(tenant_url, username, client_name):
    """ Create an Oauth client
    """
    # Set the endpoint.
    endpoint = "{}/clients/v2/{}".format(tenant_url, client_name)

    # Get user's password.                                                      
    passwd = getpass.getpass(prompt="API password: ")

    # Make request.
    try:
        resp = requests.delete(endpoint, auth=(username, passwd))
        del passwd
    except Exception as err:
        del passwd
        raise AgaveClientError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
