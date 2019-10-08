import os

ENV_PREFIX = 'TAPIS_PY'

BOOLEAN_TRUE_STRINGS = ('true', 'on', 'ok', 'y', 'yes', '1')
BOOLEAN_FALSE_STRINGS = ('false', 'off', 'n', 'no', '0')

__all__ = [
    'ns_os_environ_get', 'fix_assets_path', 'array_from_string',
    'set_from_string', 'parse_boolean', 'int_or_none', 'ENV_PREFIX'
]


def ns_os_environ_get(env_var_name, default, prefix=ENV_PREFIX):
    if prefix is not None:
        if not prefix.endswith('_'):
            prefix = prefix + '_'
    varname = '{}{}'.format(prefix, env_var_name)
    resp = os.environ.get(varname, default)
    return resp


def fix_assets_path(path):
    fullpath = os.path.join(os.path.dirname(__file__), "../", path)
    return fullpath


def array_from_string(s):
    array = s.split(',')
    if "" in array:
        array.remove("")
    return array


def set_from_string(s):
    return set(array_from_string(s))


def parse_boolean(s):
    """Takes a string and returns the equivalent as a boolean value."""
    s = s.strip().lower()
    if s in BOOLEAN_TRUE_STRINGS:
        return True
    elif s in BOOLEAN_FALSE_STRINGS:
        return False
    else:
        raise ValueError('Invalid boolean value %r' % s)


def int_or_none(value):
    if value is None:
        return value
    return int(value)
