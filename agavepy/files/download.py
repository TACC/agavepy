"""
    download.py
"""
import requests                                                                 
from .exceptions import AgaveFilesError
from ..utils import handle_bad_response_status_code



def files_download(tenant_url, access_token, source, destination):
    """ Copy a file from remote system to host

    PARAMETERS
    ----------
    """
    # Set request endpoint. 
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/media/system", source)

    # Make request.
    try:
        headers = {"Authorization":"Bearer {0}".format(access_token)}
        params  = {"pretty": "true"}

        resp = requests.get(endpoint, headers=headers, params=params, stream=True)
        with open(destination, "wb") as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    except Exception as err:
        raise AgaveFilesError(err)
        

    # Handle bad status code.                                               
    handle_bad_response_status_code(resp)
