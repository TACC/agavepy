"""
    subscribe.py

Subscribe to TACC apis
"""
import requests
from ..constants import PLATFORM
from ..utils import (handle_bad_response_status_code, prompt_username,
                     prompt_password)
from .exceptions import AgaveClientError
from .utils import clients_url


def clients_subscribe(client_name,
                      tenant_url,
                      api_name,
                      api_version,
                      api_provider,
                      username=None,
                      password=None,
                      quiet=False):
    """ Subscribe an Oauth client to an API

    PARAMETERS
    ----------
    client_name: string
        Name for the Oauth client.
    tenant_url: string
        URL of the API tenant to interact with.

    KEYWORD ARGUMENTS
    -----------------
    username: string
        The user's username.
    password: string
        The user's password.
    """
    # Set request endpoint.
    endpoint = "{0}/{1}/subscriptions".format(clients_url(tenant_url),
                                              client_name)

    # Get user's password.
    uname = prompt_username(username)
    passwd = prompt_password(password, quiet=quiet)

    # Make sure client_name is valid.
    if client_name == "" or client_name is None:
        raise AgaveClientError(
            '{0} client {1} failed: Invalid name {2}'.format(
                PLATFORM, 'subscription', client_name))

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
