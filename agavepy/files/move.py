"""
    move.py
"""
import requests
from .exceptions import AgaveFilesError
from ..utils import handle_bad_response_status_code


def files_move(tenant_url, access_token, source, destination):
    """ Copy files from remote to remote system
    """
    # Set request url.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/media/system", source)

    # Obtain file path from remote uri. "destination" should include the system
    # name at the begining, get rid of it.
    destination = '/'.join( destination.split('/')[1:] )

    # Make request.
    try:
        data = {"action": "move", "path": destination}
        headers  = {"Authorization":"Bearer {0}".format(access_token)}
        params   = {"pretty": "true"}
        resp = requests.put(endpoint, headers=headers, data=data, params=params)
    except Exception as err:
        raise AgaveFilesError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
