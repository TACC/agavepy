"""Provides a cascade of methods to establish Tapis access credentials.

For a given method, if a value is passed, it is returned. If not, the
environment is consulted, then the user is prompted interactively.
"""
from __future__ import print_function
import os
import getpass
from ..constants import (PLATFORM, ENV_USERNAME, ENV_PASSWORD, ENV_TOKEN,
                         ENV_REFRESH_TOKEN)
from .tty import print_stderr

__all__ = [
    'prompt_password', 'prompt_username', 'prompt_access_token',
    'prompt_refresh_token'
]

WARNING_MESSAGE = 'WARNING: Sending {0} via command line options is unsafe! Consider setting the {1} environment variable if you need to programmatically supply this value. Alternatively, leave the parameter empty and you will be prompted to interactively provide {0} using a secure input method.'


def prompt_password(password=None, username=None, quiet=False):
    if password is not None and password != '':
        if not quiet:
            print_stderr(WARNING_MESSAGE.format('a password', ENV_PASSWORD))
        return password
    else:
        password = os.environ.get(ENV_PASSWORD, None)
    if password is not None:
        return password
    else:
        if username is None or username == '':
            prompt = '{0} Password: '.format(PLATFORM)
        else:
            prompt = '{0} Password for {1}: '.format(PLATFORM, username)
        return getpass.getpass(prompt)


def prompt_username(username=None):
    if username is not None and username != '':
        return username
    else:
        username = os.environ.get(ENV_USERNAME, None)
    if username is not None:
        return username
    else:
        return getpass.getpass('{} Username: '.format(PLATFORM))


def prompt_access_token(access_token=None, quiet=False):
    if access_token is not None and access_token != '':
        if not quiet:
            print_stderr(WARNING_MESSAGE.format('an access token', ENV_TOKEN))
        return access_token
    else:
        access_token = os.environ.get(ENV_TOKEN, None)
    if access_token is not None:
        return access_token
    else:
        return getpass.getpass('{0} Access Token: '.format(PLATFORM))


def prompt_refresh_token(refresh_token=None, quiet=False):
    if refresh_token is not None and refresh_token != '':
        if not quiet:
            print_stderr(
                WARNING_MESSAGE.format('a refresh token', ENV_REFRESH_TOKEN))
        return refresh_token
    else:
        refresh_token = os.environ.get(ENV_REFRESH_TOKEN, None)
    if refresh_token is not None:
        return refresh_token
    else:
        return getpass.getpass('{0} Refresh Token: '.format(PLATFORM))
