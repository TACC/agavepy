"""
    list.py
"""
from __future__ import print_function, division
import py
import os
import requests
import shutil
import time
from operator import itemgetter
from .exceptions import AgaveFilesError                                         
from ..utils import handle_bad_response_status_code



file_permissions = {
    "READ"          : "-r--",
    "WRITE"         : "--w-",
    "EXECUTE"       : "---x",
    "READ_WRITE"    : "-rw-",
    "READ_EXECUTE"  : "-r-x",
    "WRITE_EXECUTE" : "--wx",
    "ALL"           : "-rwx",
    "NONE"          : "----"
}


def parse_time(ftime):
    """ Convert timestamp to local time

    Expect format: 2018-07-10T12:28:01.000-05:00

    """
    # 2018-07-10T12:28:01.000-05:00 (rm last ':')
    if ftime[-3] == ":": ftime = ftime[:-3] + ftime[-2:]

    try:
        ftime = time.strptime(ftime,'%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        tz = ftime[-5:] # get the timezone part (i.e., -0500)
        ftime = time.strptime(ftime[:-5],'%Y-%m-%dT%H:%M:%S.%f')
        if tz.startswith("-"):
            sign = -1
            tz = tz[1:] # get the hous offset
        elif tz.startswith("+"):
            tz = tz[1:] # get the hous offset
        seconds = ( int(tz[0:2])*60 + int(tz[2:4]) ) * 60
        seconds *= sign
        # Convert ftime to seconds since epoch,
        ftime = time.mktime(ftime) + seconds
        # Convert seconds since epoch to localtime.
        ftime = time.localtime(ftime)

    outtime = time.strftime("%b %d %H:%M", ftime).split()

    return ftime, outtime



def files_list(tenant_url, access_token, system_path, long_format=False):
    """ List files on a remote Agave system
    """
    # Set endpoint.
    endpoint = "{0}/{1}/{2}".format(tenant_url, "files/v2/listings/system", system_path)

    # Make request.                                                             
    try:
        headers  = {"Authorization":"Bearer {0}".format(access_token)}
        params   = {"pretty": "true"}
        resp = requests.get(endpoint, headers=headers, params=params)
    except Exception as err:
        raise AgaveFilesError(err)
    
    # Handle bad status code.
    handle_bad_response_status_code(resp)


    # Sort results alphabetically.
    resp.json()["result"] = sorted(resp.json()["result"], key=itemgetter("name"), reverse=True)

    # Get the length of the longest filename.
    longest_name = 8
    for f in resp.json()["result"]:
        if len(f["name"]) > longest_name:
            longest_name = len(f["name"])
    # Get the size fo the biggest file.
    largest_file = 0
    for f in resp.json()["result"]:
        if len(str(f["length"])) > largest_file:
            largest_file = len(str(f["length"]))

    # Get size of terminal.
    try: # python3 prefered
        terminal_size = shutil.get_terminal_size()
        terminal_size_columns = terminal_size.columns 
        columns = terminal_size.columns // longest_name
    except AttributeError:
        # _rows, columns = os.popen('stty size', 'r').read().split()
        columns = py.io.TerminalWriter().fullwidth
        terminal_size_columns = int(columns)
        columns = int(columns) // longest_name


    if not long_format:
        files = ""
        line_length = 0
        for f in resp.json()["result"]:
            name   = f["name"]
            # If directory, then append '/' to its name.
            if f["type"] == "dir":
                name += "/"

            # Give enough space to print name of file/directory.
            name += " " * (longest_name - len(name) + 3)

            # If there is not enough space in the current line to print this
            # file then move to the next line.
            if line_length + len(name) > terminal_size_columns:
                files += "\n"
                line_length = 0

            line_length += len(name)
            files += name
        
        # Print all files.
        print(files)

    else: # Print file long format.
        for f in resp.json()["result"]:
            # File permissions and name.
            name   = f["name"]

            # Set file permissions.
            perm = file_permissions[f["permissions"]]
            # Prefix perfmissions for directories with 'd'.
            if f["type"] == "dir":
                perm = "d{}".format(perm[1:])
                name += "/"
            name += " " * (longest_name - len(name) + 3)

            # File size.
            fsize = f["length"]

            # Date created.
            ftime, outtime = parse_time( f["lastModified"] )

            print("{0:<4} {1:>{size_width}} {2:<3} {3:>2} {4:<5} {5:}".format(
                    perm, fsize, outtime[0], ftime.tm_mday, outtime[2], name, 
                    size_width=largest_file))
