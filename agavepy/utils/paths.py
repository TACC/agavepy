import os
from ..constants import (SESSION_CACHE_DIRS,
                         CONFIGS_FILENAME, CLIENT_FILENAME,
                         CACHES_DIR_NAME)

__all__ = ['credentials_cache_dir', 'sessions_cache_path', 'client_cache_path']


def credentials_cache_dir(cache_dir=None, create=True):
    """Returns the path where session caches are stored.

    Unless provided with an override, environment variables defined in
    agavepy.constants.SESSION_CACHE_DIRS are interrogated, in order, to
    find a value. If no value can be determined, a default of
    $HOME/agavepy.constants.CACHES_DIR_NAME. By default, the cache directory
    is created if it does not exist.

    KEYWORD ARGUMENTS
    -----------------
    cache_dir: string
        Optional override path name for the cache directory.
    create: boolean
        Check existence of the cache directory and create it if missing.

    RETURNS
    -------
    cache_dir: string
    """
    if cache_dir is None:
        for dirname in SESSION_CACHE_DIRS:
            cache_dir = os.environ.get(dirname, None)
            if os.environ.get(dirname) is not None:
                break
    if cache_dir is None:
        cache_dir = os.path.expanduser('~/{}'.format(CACHES_DIR_NAME))
    if create:
        if not os.path.isdir(cache_dir):
            os.makedirs(cache_dir)
    return os.path.abspath(cache_dir)


def sessions_cache_path(cache_dir=None, create=True):
    """Returns path to a multi-session cache file
    """
    return os.path.join(
        credentials_cache_dir(cache_dir, create), CONFIGS_FILENAME)


def client_cache_path(cache_dir=None, create=True):
    """Returns path to a single-client cache file
    """
    return os.path.join(
        credentials_cache_dir(cache_dir, create), CLIENT_FILENAME)
