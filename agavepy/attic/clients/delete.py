"""
    clients.py
"""
import requests
from ..constants import PLATFORM
from ..utils import (handle_bad_response_status_code, prompt_username,
                     prompt_password)
from .exceptions import AgaveClientError
from .utils import clients_url


def clients_delete(tenant_url,
                   client_name,
                   username=None,
                   password=None,
                   quiet=False):
    """Deletes an Oauth client

    PARAMETERS
    ----------
    client_name: string
        Name of the Oauth client.
    tenant_url: string
        URL of the API tenant to interact with.

    KEYWORD ARGUMENTS
    -----------------
    username: string
        The user's username.
    password: string
        The user's password
    """
    # Set the endpoint.
    endpoint = "{0}/{1}".format(clients_url(tenant_url), client_name)

    # Make sure client_name is valid.
    if client_name == "" or client_name is None:
        raise AgaveClientError(
            '{0} client {1} failed: Invalid name {2}'.format(
                PLATFORM, 'deletion', client_name))

    # Get user's password.
    uname = prompt_username(username)
    passwd = prompt_password(password, quiet=quiet)

    # Make request.
    try:
        resp = requests.delete(endpoint, auth=(uname, passwd))
        del passwd
    except Exception as err:
        del passwd
        raise AgaveClientError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
