"""
    cachedir_helpers.py
"""
from __future__ import print_function
import json
import requests
import sys
import os


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


def save_config(cache_dir, current_context):
    """ Initiate an Agave Tenant

    Create or switch the current context to a specified Agave tenant.
    The current context along with all previous used are stored in a
    local database (arguments.agavedb).

    The ~/.agave/config.json file will have the following format:
        * "current" will specify the configuration to be used for the current 
          session. The contents of this section should match those of 
          ~/.agave/current.
        * "tenants" will have one or more keys, and each key will have a json 
          object related to it. Each key will correspond to a tenant id.

    For example:
    {
        "current": {
            "access_token": "some-token",
            ...
            "username": "user"
        },
        "tenants": {
            "3dem": {
                "access_token": "other-token",
                ...
                "username": "user"
            },
            "sd2e": {
                "acces_token": "some-token",
                ...
                "usernamer":user"
            }
        }
    }

    PARAMETERS
    ----------
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
        agave_context = dict()


    # Set up ~/.agave/config.json

    # We are saving configurations for the first time so we have to set 
    # "current" and add it to "tenants".
    if "tenants" not in agave_context:
        # No existing tenants, so we just add the current context.
        agave_context["current"] = current_context
        
        # Create an empty dictionary for "tenants" key.
        agave_context["tenants"] = dict()
        # Save current tenant context.
        agave_context["tenants"][current_context["tenantid"]] = agave_context["current"]
    # "tenants" already exist so we just have to put the current context
    # back in.
    else:
        # Save current tenant context.
        agave_context["tenants"][agave_context["current"]["tenantid"]] = agave_context["current"]

        # Save current_context as such.
        agave_context["current"] =  current_context


    # Save data to cache dir files.
    with open(config_file, "w") as f:
        json.dump(agave_context, f, sort_keys=True, indent=4)
    with open(current_file, "w") as f:
        json.dump(agave_context["current"], f, sort_keys=True)
