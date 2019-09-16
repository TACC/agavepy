"""
    create.py

Functions to create Agave oauth clients.
"""
from __future__ import print_function
import requests
from ..constants import PLATFORM
from ..utils import (handle_bad_response_status_code, prompt_username,
                     prompt_password)
from .exceptions import AgaveClientError
from .utils import clients_url


def clients_create(client_name,
                   description,
                   tenant_url,
                   username=None,
                   password=None,
                   quiet=False):
    """ Create an Oauth client

    Make a request to the API to create an Oauth client. Returns the client
    API key and secret as a tuple.

    PARAMETERS
    ----------
    client_name: string
        Name for Oauth client.
    description: string
        Description of the Oauth client.
    tenant_url: string
        URL of the API tenant to interact with.

    KEYWORD ARGUMENTS
    -----------------
    username: string
        The user's username.
    password: string
        The user's password

    RETURNS
    -------
    api_key: string
    api_secret: string
    """

    # Set request endpoint.
    endpoint = clients_url(tenant_url)

    # Make sure client_name is not empty
    # TODO - add additional validation to client_name
    if client_name == "" or client_name is None:
        raise AgaveClientError(
            '{0} client {1} failed: Invalid name {2}'.format(
                PLATFORM, 'creation', client_name))

    # Get user basic auth credentials
    uname = prompt_username(username)
    passwd = prompt_password(password, quiet=quiet)

    # Make request.
    try:
        data = {
            "clientName": client_name,
            "description": description,
            "tier": "Unlimited",
            "callbackUrl": "",
        }
        resp = requests.post(endpoint, data=data, auth=(uname, passwd))
        del passwd
    except Exception as err:
        del passwd
        raise AgaveClientError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)

    # Parse the request's response and return api key and secret.
    response = resp.json().get("result", {})
    api_key = response.get("consumerKey", "")
    api_secret = response.get("consumerSecret", "")
    if api_key == "" or api_secret == "":
        raise AgaveClientError(
            '{0} client {1} failed: No key/secret issued for {2}'.format(
                PLATFORM, 'creation', client_name))

    return api_key, api_secret
