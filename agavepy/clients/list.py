"""
    list.py

Functions to list agave oauth clients.
"""
from __future__ import print_function
import getpass
import requests
from .exceptions import AgaveClientError
from ..utils import handle_bad_response_status_code



def clients_list(username, tenant_url):
    """ List Oauth clients

    List all Agave oauth clients registered with the current tenant.

    PARAMETERS
    ----------
    username: string
        User's username.
    tenant_url: string
        URL of agave tenant to interact with.
    """
    # Get user's password.
    passwd = getpass.getpass(prompt="API password: ")

    # Set request endpoint.
    endpoint = tenant_url + "/clients/v2"

    # Make request.
    try:
        resp = requests.get(endpoint, auth=(username, passwd))
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
