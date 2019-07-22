"""
    list.py

Functions to list agave oauth clients.
"""
from __future__ import print_function
import requests
from ..constants import PLATFORM
from ..utils import (handle_bad_response_status_code,
                     prompt_username, prompt_password)
from .exceptions import AgaveClientError
from .utils import clients_url


def clients_list(tenant_url, username=None, password=None, quiet=False):
    """ List Oauth clients

    List all Oauth clients registered to the designated user on
    the specified tenant.

    PARAMETERS
    ----------
    tenant_url: string
        URL of the API tenant to interact with.

    KEYWORD ARGUMENTS
    -----------------
    username: string
        The user's username.
    password: string
        The user's password
    """
    # Set request endpoint.
    endpoint = clients_url(tenant_url)

    # Get user's credentials
    uname = prompt_username(username)
    passwd = prompt_password(password, quiet=quiet)

    # Make request.
    try:
        resp = requests.get(endpoint, auth=(uname, passwd))
        del passwd
    except Exception as err:
        del passwd
        raise AgaveClientError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)

    # Print results.
    print("{0:<30} {1:<80}".format("NAME", "DESCRIPTION"))
    for client in resp.json().get("result", []):
        description = client["description"] if client["description"] else ""
        print("{0:<30} {1:<80}".format(client["name"], description))
