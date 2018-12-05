"""
    import.py
"""
import requests
from .exceptions import AgaveFilesError
from ..utils import handle_bad_response_status_code


def files_import(tenant_url, access_token, source, destination):
    """ Imports a remote URI to a remote storage system

    If 'source' is an agave source then prefix the uri with 'agave://'. For 
    example, source = 'agave://data-sd2e-community/test.txt'.
    """
    # Set request url.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/media/system", destination)

    # Make request.
    try:
        # TODO: document the other fields.
        data = {
            "urlToIngest": source,
            "notifications": "",
            "fileType": "",
            "fileName": "",
        }
        headers  = {"Authorization":"Bearer {0}".format(access_token)}
        params   = {"pretty": "true"}
        resp = requests.post(endpoint, headers=headers, data=data, params=params)
    except Exception as err:
        raise AgaveFilesError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
