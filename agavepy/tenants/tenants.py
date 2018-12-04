"""
    tenants.py

Methods to interact with Agave tenants.
"""
from __future__ import print_function
import requests
import sys
from ..utils import handle_bad_response_status_code


def get_tenants(url):
    """ Get Agave tenants

    Get all Agave tenants for a given Agave host.

    PARAMETERS
    ----------
    url: string (default: "https://api.tacc.utexas.edu/tenants")
        URL to send GET request to. This resource should list all Agave
        tenants.

    RETURNS
    -------
    JSON response: dict
        If request was successful, return the json response as a dict.
    """
    # Make request.
    try:
        resp = requests.get(url)
    except Exception as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    # Handle bad status code.
    handle_bad_response_status_code(resp)

    return resp.json()


def tenant_list(tenantsurl="https://api.tacc.utexas.edu/tenants"):
    """ List Agave tenants

    List all Agave tenants for a given Agave host. Information listed is the
    name and the code of the tenant.

    PARAMETERS
    ----------
    tenantsurl: string (default: "https://api.tacc.utexas.edu/tenants") 
        Endoint to make request
    """
    # Get a json of all AGave tenants.
    tenants = get_tenants(tenantsurl)

    # Create dictionary of tenants.
    tenants_info = dict()

    # Parse results.
    for tenant in tenants.get("result", []):
        # code is the tenant id, name is the full name, baseUrl is the url.
        tenant_info = {
            "id": tenant.get("code", ""), 
            "name": tenant.get("name", ""), 
            "url": tenant.get("baseUrl", ""),
        }
        tenants_info[tenant_info["id"]] = tenant_info


    return tenants_info
