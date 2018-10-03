"""
    tokens.py

Functions to Agave access tokens. 
"""
from __future__ import print_function
import getpass
import json
import requests
import sys
import time
from os import path
from .exceptions import AgaveTokenError 
from ..utils import handle_bad_response_status_code



def token_create(username, api_key, api_secret, tenant_url):
    """ Create an access token

    PARAMETERS
    ----------
    username: string
    api_key: string
    api_secret: string
    tenant_url: string

    RETURNS
    -------
    token_data: dictionary
        Contains access_token, refresh_token, expires_in, created_at, and 
        expires_at.
    """
    # Set request endpoint.
    endpoint = "{0}{1}".format(tenant_url, "/token")

    # Make request.
    try:
        data = {
            "username": username,
            "password": getpass.getpass(prompt="API password: "),
            "grant_type": "password",
            "scope": "PRODUCTION"
        }
        params   = {"pretty": "true"}
        resp = requests.post(endpoint, data=data, params=params, auth=(api_key, api_secret))
        del data
    except Exception as err:
        del data
        raise AgaveTokenError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
    
    # Process response data.
    response = resp.json()
    now = int(time.time())
    expires_at = now + int(response.get("expires_in"))
    token_data = {
        "access_token": response.get("access_token", ""),
        "refresh_token": response.get("refresh_token", ""),
        "expires_in": response.get("expires_in", ""),
        "created_at": str(now),
        "expires_at": time.strftime("%a %b %-d %H:%M:%S %Z %Y", time.localtime(expires_at))
    }
    return token_data
