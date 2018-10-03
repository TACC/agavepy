"""
    refresh_tokens.py
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



def refresh_token(api_key, api_secret, refresh_token, tenant_url):
    """ Retrieve a new Oauth bearer token

    PARAMETERS
    ----------
    api_key: str
    api_secret: str
    refresh_token: str
    tenant_url : str

    RETURNS
    -------
    token_data: dict
        access_token: str 
        refresh_token: str 
        expires_in: str 
        created_at: str 
        expires_at: str
    """
    # Set request endpoint.
    endpoint = "{0}{1}".format(tenant_url, "/token")
    
    # Make request.
    try:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": "PRODUCTION"
        }

        resp = requests.post(endpoint, headers=headers, data=data, 
                auth=(api_key, api_secret))
    except requests.exceptions.MissingSchema as err:
        raise AgaveTokenError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)

    # Return pertinent value.
    response = resp.json()

    now = int(time.time())
    expires_at = now + int(response["expires_in"])
    
    token_data = {
        "access_token": response["access_token"],
        "refresh_token": response["refresh_token"],
        "expires_in": response["expires_in"],
        "created_at": str(now),
        "expires_at": time.strftime("%a %b %-d %H:%M:%S %Z %Y", time.localtime(expires_at))
    }

    return token_data
