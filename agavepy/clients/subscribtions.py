"""
    subscriptions.py

List oauth client subscriptions.
"""
import getpass
import requests                                                                 
from .exceptions import AgaveClientError                                        
from ..utils import handle_bad_response_status_code



def clients_subscribtions(username, client_name, tenant_url):
    """ List oauth client subscriptions
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
        resp = requests.get(endpoint, auth=(username, passwd))
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
