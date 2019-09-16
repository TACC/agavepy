from .agave import Agave

import sys # noqa
from agavepy import asynchronous # noqa
sys.modules['agavepy.async'] = asynchronous # noqa

