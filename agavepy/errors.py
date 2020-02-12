"""AgavePy errors, exceptions, and special handlers
"""

from future import standard_library
standard_library.install_aliases()  # noqa
from urllib.error import HTTPError  # noqa

__all__ = [
    'AgaveError', 'AgaveException', '__handle_tapis_error',
    '_handle_tapis_error'
]


class AgaveError(Exception):
    pass


class AgaveException(Exception):
    pass


def _handle_tapis_error(h):
    if h.code not in (400, 404):
        h.msg = h.msg + ' [{0}]'.format(h.response.text)
    raise h


def __handle_tapis_error(http_error_object):
    """Raise a more detailed HTTPError from Tapis error response
    """
    h = http_error_object
    # extract HTTP response code
    code = -1
    try:
        code = h.response.status_code
        assert isinstance(code, int)
    except Exception:
        # we have no idea what happened
        code = 418

    # extract HTTP reason
    reason = 'UNKNOWN ERROR'
    try:
        reason = h.response.reason
    except Exception:
        pass

    # Tapis APIs will give JSON responses if the target web service is at all
    # capable of fulfilling the request. Therefore, try first to extract fields
    # from the JSON response, then fall back to returning the plain text from
    # the response.
    err_msg = 'Unexpected encountered by the web service'
    status_msg = 'error'
    version_msg = 'unknown'
    try:
        j = h.response.json()
        if 'message' in j:
            err_msg = j['message']
        if 'status' in j:
            status_msg = j['status']
        if 'version' in j:
            version_msg = j['version']
    except Exception:
        err_msg = h.response.text

    httperror = '{0}'.format(err_msg)
    raise HTTPError(code, httperror)
