"""
    clients.py

Functions related to Agave Oauth clients.
"""
from __future__ import print_function
from builtins import input
import getpass
import json
import requests
import sys
from os import path
from ..utils import handle_bad_response_status_code


class AgaveClientError(Exception):
    """ Handle Agave-related client operations
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


def client_create(username, client_name, description, tenant_url):
    """ Create an Agave client

    Make a request to Agave to create an oauth client. Returns the client's api
    key and secret as a tuple.
    
    PARAMETERS
    ----------
    username: string
        User's username.
    client_name: string
        Name for agave client.
    description: string
        Description of the agave client.
    tenant_url: string
        URL of agave tenant to interact with.

    RETURNS
    -------
    api_key: string
    api_secret: string
    """
    # Get user's password.
    passwd = getpass.getpass(prompt="API password: ")

    # Set request endpoint.
    endpoint = tenant_url + "/clients/v2"

    # Make sure client_name is valid.
    if client_name == "" or client_name is None:
        raise AgaveClientError("Error creating client: invalid client_name")

    # Make request.
    try:
        data = {
            "clientName": client_name,
            "description": description,
            "tier": "Unlimited",
            "callbackUrl": "",
        }
        resp = requests.post(endpoint, data=data, auth=(username, passwd))
        del passwd
    except Exception as err:
        del passwd
        raise AgaveClientError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)

    # Parse the request's response and return api key and secret.
    response   = resp.json().get("result", {})
    api_key    = response.get("consumerKey", "")
    api_secret = response.get("consumerSecret", "")
    if api_key == "" or api_secret == "":
        raise AgaveClientError("Error creating client: api key and secret are empty")

    return api_key, api_secret
