"""Provides a cascade of methods to establish Tapis access credentials.

For a given method, if a value is passed, it is returned. If not, the
environment is consulted, then the user is prompted interactively.
"""
from __future__ import print_function
import os
import sys
import getpass

__all__ = ['get_password', 'get_username',
           'load_access_token', 'load_refresh_token', 'print_stderr']


def print_stderr(message):
    print(message, file=sys.stderr)


def get_password(password=None, username=None, quiet=False):
    if password is not None and password != '':
        # raise SystemError(quiet)
        if not quiet:
            print_stderr('WARNING: Sending a password via command line options is unsafe! Consider setting the TAPIS_PASSWORD environment variable if you need to automatically supply a password to Tapis. Alternatively, leave off the command line option and you will be prompted to enter a password using a secure input method.')
        return password
    else:
        password = os.environ.get(
            'TAPIS_PASSWORD', None)
    if password is not None:
        return password
    else:
        if username is None or username == '':
            prompt = 'API Password: '
        else:
            prompt = 'API Password for {}: '.format(username)
        return getpass.getpass(prompt)


def get_username(username=None):
    if username is not None and username != '':
        return username
    else:
        username = os.environ.get(
            'TAPIS_USERNAME', None)
    if username is not None:
        return username
    else:
        return getpass.getpass('API Username: ')


def load_access_token(access_token=None, quiet=False):
    if access_token is not None and access_token != '':
        if not quiet:
            print_stderr('WARNING: Sending an access token via command line options is unsafe! Consider setting the TAPIS_ACCESS_TOKEN environment variable if you need to automatically supply a token to Tapis. Alternatively, leave off the command line option and you will be prompted to enter the access token using a secure input method.')
        return access_token
    else:
        access_token = os.environ.get(
            'TAPIS_ACCESS_TOKEN', None)
    if access_token is not None:
        return access_token
    else:
        return getpass.getpass('API Access Token: ')


def load_refresh_token(refresh_token=None, quiet=False):
    if refresh_token is not None and refresh_token != '':
        if not quiet:
            print_stderr('WARNING: Sending a refresh token via command line options is unsafe! Consider setting the TAPIS_REFRESH_TOKEN environment variable if you need to automatically supply a refresh token to Tapis. Alternatively, leave off the command line option and you will be prompted to enter the refresh token using a secure input method.')
        return refresh_token
    else:
        refresh_token = os.environ.get(
            'TAPIS_REFRESH_TOKEN', None)
    if refresh_token is not None:
        return refresh_token
    else:
        return getpass.getpass('API Refresh Token: ')
