"""
    pems_list.py
"""
import requests
from .exceptions import AgaveFilesError
from ..utils import handle_bad_response_status_code


def files_pems_list(tenant_url, access_token, path):
    """ List the user permissions associated with a file or folder. 
    
    These permissions are set at the API level and do not reflect *nix or other
    file system ACL.
    """
    # Set request url.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/pems/system", path)

    # Obtain file path. "path" should include the system name at the begining,
    # so we get rid of it.
    destination = '/'.join( path.split('/')[1:] )

    # Make request.
    try:
        headers  = {"Authorization":"Bearer {0}".format(access_token)}
        params   = {"pretty": "true"}
        resp = requests.get(endpoint, headers=headers, params=params)
    except Exception as err:
        raise AgaveFilesError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)

    print("{0:<13} {1:<6} {2:<6} {3:<6}".format("USER", "READ", "WRITE", "EXEC"))
    for pems in resp.json()["result"]:
        r = pems["permission"]["read"]
        w = pems["permission"]["write"]
        e = pems["permission"]["execute"]
        r = "yes" if r else "no"
        w = "yes" if w else "no"
        e = "yes" if e else "no"

        print("{0:<13} {1:<6} {2:<6} {3:<6}".format(pems["username"], r, w, e))
