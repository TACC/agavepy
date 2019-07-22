from __future__ import print_function
import sys

__all__ = ['print_stderr']


def print_stderr(message):
    """Prints a message to STDERR
    """
    print(message, file=sys.stderr)
