"""Utilities for working with Tapis tenants
"""
import requests
from .. import settings

__all__ = ['list_tenants', 'api_server_by_id']


def list_tenants(url=None):
    """List available Tapis tenants

    Returns all tenants configured in a Tapis instance.

    PARAMETERS
    ----------
    url: string (default: "https://api.tacc.utexas.edu/tenants")
        URL to send GET request to. This resource should list all tenants.

    RETURNS
    -------
    JSON response: dict
        If request was successful, return the json response as a dict.
    """
    if url is None:
        url = settings.TENANTS_URL

    try:
        resp = requests.get(url)
        resp.raise_for_status()
    except Exception:
        raise

    return resp.json().get('result', [])


def api_server_by_id(tenant_id, url=None):
    """Resolve Tapis tenant ID to its API server
    """
    tenants = list_tenants(url)
    for t in tenants:
        if t.get('code').lower() == tenant_id.lower():
            return t.get('baseUrl')
