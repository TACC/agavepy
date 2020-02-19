__all__ = ['TokenCommands']


class TokenCommands(object):
    def refresh(self):
        """If possible, attempt to refresh the Oauth token

        This is the function that should be used to 
        regenerate an Oauth token as it can deal with 
        cases where no refresh capability is configured. 
        """
        if getattr(self, 'token') is not None:
            return self.token.refresh()
        else:
            if not self.can_refresh:
                return getattr(self, '_token', None)
            else:
                raise Exception(
                    'Oauth client is not configured to refresh tokens')

    def tokens(self):
        """Return current access and refresh tokens
        """
        resp = {}
        resp['access_token'] = getattr(self, '_token', None)
        resp['refresh_token'] = getattr(self, 'refresh_token', None)
        return resp
