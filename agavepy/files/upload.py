"""
    upload.py
"""
from __future__ import print_function
import ntpath
import os
import requests
from requests_toolbelt import MultipartEncoder
from .exceptions import AgaveFilesError
from ..utils import handle_bad_response_status_code



#def cp_local_to_remote(origin, destination, tenant_url, headers, params):
def files_upload(tenant_url, access_token, source, destination):
    """ Upload a file to remote Agave system
    """
    # Get absolute path for local file.
    file_path = os.path.abspath(source)

    # Remove '/' from begining of it exists.
    if destination[0] == '/': destination = destination[1:]

    # Remove system name from destination.
    system_name     = destination.split('/')[0]
    remote_filename = '/'.join( destination.split('/')[1:] )
    if remote_filename == '' or remote_filename[-1] == '/':
        remote_filename = ntpath.basename(file_path)

    # Set request endpoint.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/media/system", destination)

    try:
        m = MultipartEncoder(
            fields={"fileToUpload":
                    (remote_filename, open(file_path, "rb"), "text/plain")}
        )
        
        headers = {
            "Authorization":"Bearer {0}".format(access_token),
            "Content-Type": m.content_type
        }
        
        resp = requests.post(endpoint, data=m, headers=headers)
    except Exception as err:
        raise AgaveFilesError(err)
                
    # Handle bad status code.
    handle_bad_response_status_code(resp)
