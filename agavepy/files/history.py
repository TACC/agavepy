"""
    history.py
"""
import requests
from .exceptions import AgaveFilesError
from ..utils import handle_bad_response_status_code


def files_history(tenant_url, access_token, path):
    """ List the history of events for a specific file/folder
    """
    # Set request url.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/history/system", path)

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

    print("{0:<13} {1:<20} {2:<32} {3:<}".format("USER", "EVENT", "DATE", "DESCRIPTION"))
    for msg in resp.json()["result"]:
        user        = msg["createdBy"]
        event       = msg["status"]
        date        = msg["created"]
        description = msg["description"]

        print("{0:<13} {1:<20} {2:<32} {3:<}".format(user, event, date, description))
