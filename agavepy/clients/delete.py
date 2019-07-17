"""
    clients.py
"""
import requests
from .exceptions import AgaveClientError
from ..utils import (handle_bad_response_status_code,
                     get_username, get_password)


def clients_delete(tenant_url, client_name,
                   username=None, password=None, quiet=False):
    """Deletes a Tapis Oauth client

    PARAMETERS
    ----------
    client_name: string
        Plaintext name for the Oauth client.
    tenant_url: string
        URL of agave tenant to interact with.

    KEYWORD ARGUMENTS
    -----------------
    username: string
        The user's username. If the API username is not passed as a keyword
        argument, it will be retrieved from the environment variable
        TAPIS_USERNAME. If the variable is not set, the user is
        prompted interactively for a value.

    password: string
        The user's password. If the API username is not passed as a keyword
        argument, it will be retrieved from the environment variable
        TAPIS_PASSWORD. If the variable is not set, the user is
        prompted interactively for a value.
    """
    # Make sure client_name is valid.
    if client_name == "" or client_name is None:
        raise AgaveClientError("Error accessing client: invalid client_name")

    # Set the endpoint.
    endpoint = "{}/clients/v2/{}".format(tenant_url, client_name)

    # Get user's password.
    uname = get_username(username)
    passwd = get_password(password, quiet=quiet)

    # Make request.
    try:
        resp = requests.delete(endpoint, auth=(uname, passwd))
        del passwd
    except Exception as err:
        del passwd
        raise AgaveClientError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
