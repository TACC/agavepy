"""
    pems_update.py
"""
import requests
from .exceptions import AgaveFilesError
from ..utils import handle_bad_response_status_code


def files_pems_update(tenant_url, access_token, path, username, perms, recursive=False):
    """ Edit user permissions associated with a file or folder. 
    
    These permissions are set at the API level and do not reflect *nix or other
    file system ACL.
    Deletes all permissions on a file except those of the owner.
    Valid values for setting permission with the -P flag are READ, WRITE, 
    EXECUTE, READ_WRITE, READ_EXECUTE, WRITE_EXECUTE, ALL, and NONE.
    """
    # Set request url.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/pems/system", path)

    # Obtain file path. "path" should include the system name at the begining,
    # so we get rid of it.
    destination = '/'.join( path.split('/')[1:] )

    # Make request.
    try:
        headers  = {"Authorization":"Bearer {0}".format(access_token)}
        data     = {
            "username": username, 
            "permission": perms, 
            "recursive": recursive
        }
        params   = {"pretty": "true"}
        resp = requests.post(endpoint, headers=headers, data=data, params=params)
    except Exception as err:
        raise AgaveFilesError(err)

    # Handle bad status code.
    handle_bad_response_status_code(resp)
