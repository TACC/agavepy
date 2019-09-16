import os
import pytest
from .fixtures import *

PWD = os.getcwd()
HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
TESTS_DATA = os.path.join(PARENT, 'data')


def pytest_addoption(parser):
    parser.addoption('--smoketest',
                     action='store_true',
                     dest='smoketest',
                     default=False,
                     help='Run ONLY smoke tests (@smoketest)')
    parser.addoption('--longrun',
                     action='store_true',
                     dest='longrun',
                     default=False,
                     help='Include tests that take a long time (@longrun)')


def pytest_runtest_setup(item):
    if item.config.getvalue('smoketest') is True:
        if 'smoketest' not in item.keywords:
            pytest.skip('not a smoketest')
    if 'longrun' in item.keywords and not item.config.getvalue('longrun'):
        pytest.skip('needs --longrun option to run')
