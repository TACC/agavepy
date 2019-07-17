"""
    create.py

Functions to create Agave oauth clients.
"""
from __future__ import print_function
import requests
from .exceptions import AgaveClientError
from ..utils import (handle_bad_response_status_code,
                     get_username, get_password)


def clients_create(client_name, description, tenant_url,
                   username=None, password=None, quiet=False):
    """ Create a Tapis Oauth client

    Make a request to Agave to create an oauth client. Returns the client's api
    key and secret as a tuple.

    PARAMETERS
    ----------
    tenant_url: string
        URL of agave tenant to interact with.

    PARAMETERS
    ----------
    client_name: string
        Name for agave client.
    description: string
        Description of the agave client.
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

    RETURNS
    -------
    api_key: string
    api_secret: string
    """

    # Set request endpoint.
    endpoint = tenant_url + "/clients/v2"

    # Make sure client_name is not empty
    # TODO - add additional validation to client_name
    if client_name == "" or client_name is None:
        raise AgaveClientError("Error creating client: Invalid client_name")

    # Get user basic auth credentials
    uname = get_username(username)
    passwd = get_password(password, quiet=quiet)

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
            "Error creating client: Tapis API key and secret will be empty")

    return api_key, api_secret
