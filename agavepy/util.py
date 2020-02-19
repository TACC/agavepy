"""General utility functions
"""
import socket
import logging
import petname
import os
import requests
import socket
import xml.etree.ElementTree as ElementTree

from functools import wraps

logger = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(
    os.environ.get('TAPISPY_LOG_LEVEL', logging.WARNING))

__all__ = [
    'AttrDict', 'json_response', 'with_refresh', 'clients_url',
    'random_client_name'
]


class AttrDict(dict):
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


def json_response(f):
    @wraps(f)
    def _f(*args, **kwargs):
        resp = f(*args, **kwargs)
        resp.raise_for_status()
        return resp.json()

    return _f


def with_refresh(client, f, *args, **kwargs):
    """Call function ``f`` and refresh token if needed."""
    logger.debug('with_refresh()...')
    try:
        return f(*args, **kwargs)
    except requests.exceptions.HTTPError as exc:
        logger.debug('HTTPError: {0}'.format(exc))
        try:
            # Old versions of APIM return errors in XML:
            code = ElementTree.fromstring(exc.response.text)[0].text
            # raise SystemError(code)
        except Exception:
            # Any error here means the response was not XML.
            try:
                # Try to see if it's a json response,
                exc_json = exc.response.json()
                # if so, check if it is an expired token error (new versions of APIM return JSON errors):
                if "Invalid Credentials" in exc_json.get("fault").get(
                        "message"):
                    logger.info('client.refresh() and retry...')
                    #client.token.refresh()
                    client.refresh()
                    return f(*args, **kwargs)
                #  otherwise, return the JSON
                return exc.response
            except Exception:
                # Re-raise it, as it's not an expired token
                raise exc
        # only catch 'token expired' exception
        # other codes may mean a different error
        if code not in ["900903", "900904"]:
            logger.error('Unexpected error code: {0}'.format(code))
            raise

        if client.can_refresh:
            logger.info('Fallback: client.token.refresh() and retry...')
            client.refresh()

        return f(*args, **kwargs)


def clients_url(tenant_url):
    """Returns the clients API endpoint for a given tenant
    """
    return '{0}/clients/v2'.format(tenant_url)


def random_client_name(words=3, letters=6, hostname=False):
    """Generate a pseudorandom but human-readable Oauth client name
    """
    client_name = petname.generate(words=words, letters=letters)
    if hostname:
        client_name = socket.gethostname().lower() + '-' + client_name
    return client_name
