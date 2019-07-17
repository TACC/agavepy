"""
    subscribe.py

Subscribe to TACC apis
"""
import requests
from .exceptions import AgaveClientError
from ..utils import (handle_bad_response_status_code,
                     get_username, get_password)


def clients_subscribe(client_name, tenant_url,
                      api_name, api_version, api_provider,
                      username=None, password=None, quiet=False):
    """ Subscribe a Tapis Oauth client to an API

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
    # Set request endpoint.
    endpoint = "{}/clients/v2/{}/subscriptions".format(tenant_url, client_name)

    # Get user's password.
    uname = get_username(username)
    passwd = get_password(password, quiet=quiet)

    # Make sure client_name is valid.
    if client_name == "" or client_name is None:
        raise AgaveClientError("Error accessing client: invalid client_name")

    # Make request.
    try:
        data = {
            "apiName": api_name,
            "apiVersion": api_version,
            "apiProvider": api_provider,
        }
        resp = requests.post(endpoint, data=data, auth=(uname, passwd))
        del passwd
    except Exception as err:
        del passwd
        raise AgaveClientError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
