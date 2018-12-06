"""
    mkdir.py
"""
import requests
from .exceptions import AgaveFilesError
from ..utils import handle_bad_response_status_code


def files_mkdir(tenant_url, access_token, location):
    """ Create an empty directory on a remote storage system
    """
    # Separate system and location.
    system = location.split('/')[0]
    location = '/'.join( location.split('/')[1:] )

    # Set request url.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/media/system", system)

    # Make request.
    try:
        data = {"action": "mkdir", "path": location}
        headers  = {"Authorization":"Bearer {0}".format(access_token)}
        params   = {"pretty": "true"}
        resp = requests.put(endpoint, headers=headers, data=data, params=params)
    except Exception as err:
        raise AgaveFilesError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
