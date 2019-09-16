"""Public, low-dependency helper functions
"""
import arrow
import os
import pkg_resources
import six

from dateutil.parser import parse


def ts_to_isodate(date_string, include_time=False):
    """Convert a datetime string (UTC) into a date string in ISO format"""

    iso_date_str = date_string

    try:
        date = parse(date_string)
        if include_time:
            if six.PY3:
                iso_date_str = date.isoformat(timespec='seconds')
            else:
                iso_date_str = date.isoformat()
        else:
            iso_date_str = date.date().isoformat()
    except ValueError:
        pass

    return iso_date_str


def ts_to_date(date_string):
    """Convert a datetime string (UTC) into a pretty date string"""

    date_rep = date_string

    try:
        date = parse(date_string)
        date_rep = date.strftime('%b %d %H:%M:%S %Y')
    except ValueError:
        pass

    return date_rep


def datetime_to_isodate(date_obj):
    """Convert a Python datetime object to ISO-8601
    """
    return arrow.get(date_obj).format('YYYY-MM-DDTHH:mm:ss.SSSZZ')


def datetime_to_human(date_obj):
    """Convert a Python datetime object to a human-friendly string
    """
    return arrow.get(date_obj).humanize()


def humanize_bytes(bytesize, precision=2):
    """
    Humanize byte size figures
    """
    # Reference: https://gist.github.com/moird/3684595

    abbrevs = ((1 << 50, 'PB'), (1 << 40, 'TB'), (1 << 30, 'GB'),
               (1 << 20, 'MB'), (1 << 10, 'kB'), (1, 'bytes'))
    if bytesize == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytesize >= factor:
            break
    if factor == 1:
        precision = 0
    return '%.*f %s' % (precision, bytesize / float(factor), suffix)
