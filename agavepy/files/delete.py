"""
    delete.py
"""
import requests
from .exceptions import AgaveFilesError                                         
from ..utils import handle_bad_response_status_code



def files_delete(tenant_url, access_token, file_path):
    """ Remove a file or direcotry from a remote system
    """
    # Set request url.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/media/system", file_path)

    # Make request.
    try:
        headers  = {"Authorization":"Bearer {0}".format(access_token)}
        params   = {"pretty": "true"}
        resp = requests.delete(endpoint, headers=headers, params=params)
    except Exception as err:
        raise AgaveFilesError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
