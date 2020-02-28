"""Token management
"""

import logging
import os
import requests
import time

from future import standard_library
standard_library.install_aliases()  # noqa
from urllib.parse import urlparse, urlencode, urljoin, urlsplit  # noqa

from agavepy.constants import (CACHES_DOT_DIR, AGPY_FILENAME, CACHE_FILENAME,
                               SESSIONS_FILENAME, TOKEN_SCOPE, TOKEN_TTL,
                               ENV_BASE_URL, ENV_TOKEN, ENV_REFRESH_TOKEN,
                               ENV_USERNAME, ENV_PASSWORD, ENV_API_KEY,
                               ENV_API_SECRET, ENV_TENANT_ID)

logger = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(
    os.environ.get('TAPISPY_LOG_LEVEL', logging.WARNING))

__all__ = ['Token']


class Token(object):
    def __init__(
            self,
            username,
            password,
            api_server,
            api_key,
            api_secret,
            verify,
            parent,
            _token=None,
            _refresh_token=None,
            token_username=None,
            expires_at=None,
            expires_in=None,
            created_at=None,
    ):
        self.username = username
        self.password = password
        self.api_server = api_server
        self.api_key = api_key
        self.api_secret = api_secret
        self.token_username = token_username
        # Agave object that created this token
        self.parent = parent
        self.verify = verify
        if _token and _refresh_token:
            self.token_info = {
                "access_token": _token,
                "refresh_token": _refresh_token
            }
            self.token_info["expires_at"] = expires_at
            self.token_info["expires_in"] = expires_in
            self.token_info["created_at"] = created_at
            self.parent._token = _token

        self.token_url = urljoin(str(self.api_server), "token")
        logger.debug('Token URL: {0}'.format(self.token_url))

    def _token(self, data):
        logger.debug('Token._token({0})...'.format(data))
        auth = requests.auth.HTTPBasicAuth(self.api_key, self.api_secret)
        resp = requests.post(
            self.token_url,
            data=data,
            auth=auth,
            verify=self.verify,
            proxies=self.parent.proxies,
        )
        resp.raise_for_status()
        self.token_info = resp.json()
        logger.debug('self.token_info: {0}'.format(self.token_info))

        # The following enforces a maximum *reported* token TTL
        #
        # For clients that consult the expiration data in the auth
        # cache to determine whether to refresh, this will solve most of
        # their credential expiry issues
        expires_in = int(self.token_info.get("expires_in", TOKEN_TTL))
        if expires_in > TOKEN_TTL:
            expires_in = TOKEN_TTL
        logger.debug('expires_in: {0} seconds'.format(expires_in))

        created_at = int(time.time())
        self.token_info["expires_in"] = expires_in
        self.token_info["created_at"] = created_at
        self.token_info["expiration"] = created_at + expires_in
        self.token_info["expires_at"] = time.ctime(created_at + expires_in)
        token = self.token_info["access_token"]
        logger.debug('token: {0}'.format(token))

        # Update parent with new token data
        self.parent._token = token
        self.parent.refresh_token = self.token_info["refresh_token"]
        self.parent.created_at = self.token_info["created_at"]
        self.parent.expiration = self.token_info["expiration"]
        self.parent.expires_at = self.token_info["expires_at"]
        self.parent.expires_in = self.token_info["expires_in"]

        # try to persist the token data
        try:
            self.parent._write_client()
        except Exception as exc:
            # failing to writing the cache file cannot block use.
            logger.warning('Failed to write client: {0}'.format(exc))
            pass

        if self.parent.token_callback:
            self.parent.token_callback(**self.token_info)
        self.parent.refresh_aris()
        return token

    def create(self):
        logger.debug('Token.create()...')
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "scope": TOKEN_SCOPE,
        }
        if self.token_username:
            data["grant_type"] = "admin_password"
            data["token_username"] = self.token_username

        return self._token(data)

    def refresh(self):
        logger.debug('Token.refresh()...')
        data = {
            "grant_type": "refresh_token",
            "scope": TOKEN_SCOPE,
            "refresh_token": self.token_info["refresh_token"],
        }

        logger.debug('Token.refresh() finished')
        return self._token(data)
