"""Stub support for 0.9.x experimental interactive commands
"""

DISCONTINUED_MSG = 'This function is discontinuted. Consult the Tapis CLI Python API for an analogous capability.'

__all__ = ['DiscontinuedError', 'InteractiveCommands']


class DiscontinuedError(NotImplementedError):
    def __init__(self):
        NotImplementedError.__init__(self, DISCONTINUED_MSG)


class InteractiveCommands(object):
    def init(self, tenantsurl=None):
        raise DiscontinuedError

    def save_configs(self, cache_dir=None):
        raise DiscontinuedError

    def load_configs(self,
                     cache_dir=None,
                     tenant_id=None,
                     username=None,
                     client_name=None):
        raise DiscontinuedError

    def load_client(self,
                    cache_dir=None,
                    tenant_id=None,
                    username=None,
                    client_name=None):
        raise DiscontinuedError

    def list_tenants(self, tenantsurl=None):
        raise DiscontinuedError

    def clients_create(self,
                       client_name,
                       description,
                       username=None,
                       password=None,
                       quiet=False):
        raise DiscontinuedError

    def clients_delete(self,
                       client_name=None,
                       username=None,
                       password=None,
                       quiet=False):
        raise DiscontinuedError

    def clients_subscribe(self,
                          api_name,
                          api_version,
                          api_provider,
                          client_name=None,
                          username=None,
                          password=None,
                          quiet=False):
        raise DiscontinuedError

    def clients_subscriptions(self,
                              client_name=None,
                              username=None,
                              password=None,
                              quiet=False):
        raise DiscontinuedError

    def clients_list(self, username=None, password=None, quiet=False):
        raise DiscontinuedError

    def get_access_token(self, username=None, password=None, quiet=False):
        raise DiscontinuedError

    def refresh_tokens(self, force=False):
        raise DiscontinuedError

    def files_copy(self, source, destination):
        raise DiscontinuedError

    def files_delete(self, file_path):
        raise DiscontinuedError

    def files_download(self, source, destination):
        raise DiscontinuedError

    def files_history(self, path):
        raise DiscontinuedError

    def files_import(self, source, destination):
        raise DiscontinuedError

    def files_list(self, system_path, long_format=False):
        raise DiscontinuedError

    def files_mkdir(self, location):
        raise DiscontinuedError

    def files_move(self, source, destination):
        raise DiscontinuedError

    def files_pems_delete(self, path):
        raise DiscontinuedError

    def files_pems_list(self, path):
        raise DiscontinuedError

    def files_pems_update(self, path, username, perms, recursive=False):
        raise DiscontinuedError

    def files_upload(self, source, destination):
        raise DiscontinuedError
