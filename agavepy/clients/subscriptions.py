"""
    subscriptions.py

List Oauth client subscriptions.
"""
import requests
from .exceptions import AgaveClientError
from ..utils import (handle_bad_response_status_code,
                     get_username, get_password)


def clients_subscriptions(client_name, tenant_url,
                          username=None, password=None, quiet=False):
    """ List Tapis Oauth client subscriptions

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
    # Make sure client_name is valid.
    if client_name == "" or client_name is None:
        raise AgaveClientError("Error accessing client: invalid client_name")

    # Set request endpoint.
    endpoint = "{}/clients/v2/{}/subscriptions".format(tenant_url, client_name)

    # Get user basic auth credentials
    uname = get_username(username)
    passwd = get_password(password, quiet=quiet)

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
    print("{0:<16} {1:^8} {2:<20}".format("NAME", "VERSION", "PROVIDER"))
    for api in resp.json().get("result", []):
        print("{0:<16} {1:^8} {2:<20}".format(
            api["apiName"], api["apiVersion"], api["apiProvider"]))
