"""
    exceptions.py
"""


class AgaveFilesError(Exception):
    """ Handle files-related operation errors
    """
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return repr(self.msg)
