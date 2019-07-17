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
from ..utils import (handle_bad_response_status_code,
                     get_username, get_password)


def token_create(api_key, api_secret, tenant_url,
                 username=None, password=None, quiet=False):
    """ Create an access token

    PARAMETERS
    ----------
    api_key: string
    api_secret: string
    tenant_url: string

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
    token_data: dictionary
        Contains access_token, refresh_token, expires_in, created_at, and
        expires_at.
    """

    # Set request endpoint.
    endpoint = "{0}{1}".format(tenant_url, "/token")

    # Get user basic auth credentials
    uname = get_username(username)
    passwd = get_password(password, username=uname, quiet=quiet)

    # Make request.
    try:
        data = {
            "username": uname,
            "password": passwd,
            "grant_type": "password",
            "scope": "PRODUCTION"
        }
        params = {"pretty": "true"}
        resp = requests.post(endpoint, data=data,
                             params=params, auth=(api_key, api_secret))
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
