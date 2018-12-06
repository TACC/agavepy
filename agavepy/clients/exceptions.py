"""
    exceptions.py
"""


class AgaveClientError(Exception):
    """ Handle Agave-related client operations
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
