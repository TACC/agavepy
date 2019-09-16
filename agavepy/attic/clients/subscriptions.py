"""
    subscriptions.py

List Oauth client subscriptions.
"""
import requests
from ..constants import PLATFORM
from ..utils import (handle_bad_response_status_code, prompt_username,
                     prompt_password)
from .exceptions import AgaveClientError
from .utils import clients_url


def clients_subscriptions(client_name,
                          tenant_url,
                          username=None,
                          password=None,
                          quiet=False):
    """ List Oauth client subscriptions

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

    # Make sure client_name is valid.
    if client_name == "" or client_name is None:
        raise AgaveClientError(
            '{0} client {1} failed: Invalid name {2}'.format(
                PLATFORM, 'subscription listing', client_name))

    # Get user basic auth credentials
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
    print("{0:<16} {1:^8} {2:<20}".format("NAME", "VERSION", "PROVIDER"))
    for api in resp.json().get("result", []):
        print("{0:<16} {1:^8} {2:<20}".format(api["apiName"],
                                              api["apiVersion"],
                                              api["apiProvider"]))
