"""
    save_configs.py
"""
from __future__ import print_function
import json
import requests
import sys
import os
from collections import defaultdict



def make_cache_dir(cache_dir):
    """ Create cache dir

    Create agave cache dir in in the specified location, if it doesn't already
    exist.

    PARAMETERS
    ----------
    cache_dir: str
        Location to make cache dir.
    """
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)


def save_config(cache_dir, current_context, client_name):
    """ Save session configurations to file.

    Create or switch the current session context.

    The ~/.agave/config.json file will have the following format:
        * "current" will specify the configuration to be used for the current 
          session. The contents of this section should include a nested json 
          object wich will hold all session configurations. It matches the 
          information of ~/.agave/current.
        * "sessions" will be a series of nested json objects. Each session 
        configuration will be indexed by tenant id, user name, and client name,
        respectively.

    For example:
    {
        "current": {
            "client-name": {
                "access_token": "some-token",
                ...
                "username": "user"
            }
        },
        "sessions": {
            "3dem": {
                "username": {
                    "client-name": {
                        "access_token": "other-token",
                        ...
                        "username": "user"
                    },
                    "client-name-2": {
                        "access_token": "some-other-token",
                        ...
                        "username"
                    }
                }
            },
            "sd2e": {
                "username": {
                    "client-name": {
                        "acces_token": "some-token",
                        ...
                        "usernamer":user"
                    }
                }
            }
        }
    }

    PARAMETERS
    ----------
    cache_dir: string
        Path to store session configuration.
    current_context: dict
        Session context.
    client_name: string
        Name of oauth client being used in the current session.
    """
    # Get location to store configuration.
    make_cache_dir(cache_dir)
    current_file = "{}/current".format(cache_dir)
    config_file = "{}/config.json".format(cache_dir)
    config_files = [current_file, config_file]


    # Read in configuration from cache dir if it exist, else create one.
    if os.path.isfile(config_file):
        with open(config_file, "r") as f:
            agave_context = json.load(f)
    else:
        agave_context = defaultdict(lambda: defaultdict(dict))


    # Set up ~/.agave/config.json

    # We are saving configurations for the first time so we have to set 
    # "current" and add it to "tenants".
    if "sessions" not in agave_context:
        # No current session, so we just add the current context.
        agave_context["current"][client_name] = current_context
        
        # Save current tenant context.
        tenant_id = current_context["tenantid"]
        username  = current_context["username"]

        # Initialize fields as appropiate.
        # Will save the saved current context, this already includes the client
        # name.
        agave_context["sessions"][tenant_id][username] = \
            agave_context["current"]
    # There are existing sessions already so we just have to properly save the
    # current context.
    else:
        # Save current tenant context to sessions.
        # The saved client should be the only entry in the current session.
        saved_client = list(agave_context["current"].keys())[0]
        tenant_id = agave_context["current"][saved_client]["tenantid"]
        username  = agave_context["current"][saved_client]["username"]
        
        # Initialized sessions fields if they don't already exist.
        if tenant_id not in agave_context["sessions"].keys():
            agave_context["sessions"][tenant_id] = dict()
        if username not in agave_context["sessions"][tenant_id].keys():
            agave_context["sessions"][tenant_id][username] = dict()

        # Save current context on sessions.
        agave_context["sessions"][tenant_id][username][saved_client] = \
            agave_context["current"][saved_client]

        # Save "current_context".
        del agave_context["current"][saved_client]
        agave_context["current"][client_name] =  current_context


    # Save data to cache dir files.
    with open(config_file, "w") as f:
        json.dump(agave_context, f, indent=4)
    with open(current_file, "w") as f:
        json.dump(agave_context["current"][client_name], f, sort_keys=True)
