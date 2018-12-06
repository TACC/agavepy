"""
    subscribe.py

Subscribe to TACC apis
"""
import getpass
import requests                                                                 
from .exceptions import AgaveClientError                                        
from ..utils import handle_bad_response_status_code



def clients_subscribe(username, client_name, tenant_url, 
        api_name, api_version, api_provider):
    """ Subscribe an oauth client to an api
    """
    # Set request endpoint.
    endpoint = "{}/clients/v2/{}/subscriptions".format(tenant_url, client_name)

    # Get user's password.
    passwd = getpass.getpass(prompt="API password: ")

    # Make sure client_name is valid.
    if client_name == "" or client_name is None:
        raise AgaveClientError("Error creating client: invalid client_name")

    # Make request.
    try:
        data = {
            "apiName": api_name,
            "apiVersion": api_version,
            "apiProvider": api_provider,
        }
        resp = requests.post(endpoint, data=data, auth=(username, passwd))
        del passwd
    except Exception as err:
        del passwd
        raise AgaveClientError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
