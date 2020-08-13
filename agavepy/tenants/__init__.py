"""Utilities for working with Tapis tenants
"""
from agavepy.settings import TAPIS_TENANTS_URL, TAPISPY_VERIFY_SSL
import requests

__all__ = ['list_tenants', 'api_server_by_id', 'id_by_api_server']


# TODO - Cache with functools lru_cache
def list_tenants(url=None, verify_ssl=TAPISPY_VERIFY_SSL):
    """List available Tapis tenants

    Returns all tenants configured in a Tapis instance.

    PARAMETERS
    ----------
    url: string (default: settings.TAPIS_TENANTS_URL)
        URL to send GET request to. This resource should list all tenants.

    RETURNS
    -------
    JSON response: dict
        If request was successful, return the json response as a dict.
    """
    if url is None:
        url = TAPIS_TENANTS_URL

    try:
        resp = requests.get(url, verify=verify_ssl)
        resp.raise_for_status()
    except Exception:
        raise

    tenants = resp.json().get('result', [])
    resp.close()
    return tenants


def api_server_by_id(tenant_id, url=None, verify_ssl=TAPISPY_VERIFY_SSL):
    """Resolve Tapis tenant ID to its API server
    """
    tenants = list_tenants(url, verify_ssl=verify_ssl)
    for t in tenants:
        if t.get('code').lower() == tenant_id.lower():
            return t.get('baseUrl')


def id_by_api_server(api_server, url=None, verify_ssl=TAPISPY_VERIFY_SSL):
    """Resolve tenant id by its API server
    """
    tenants = list_tenants(url, verify_ssl=verify_ssl)
    for t in tenants:
        # TODO - ignore presence/absence of trailing slash
        if t.get('baseUrl').lower() == api_server.lower():
            return t.get('code')
