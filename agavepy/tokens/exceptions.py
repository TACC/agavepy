"""
    exceptions.py
"""


class AgaveTokenError(Exception):
    """ Handle Agave-related token operation errors
    """
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return repr(self.msg)
