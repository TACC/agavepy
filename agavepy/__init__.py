from .agave import Agave

import sys

from agavepy import asynchronous
sys.modules['agavepy.async'] = asynchronous
