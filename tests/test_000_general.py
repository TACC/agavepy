__author__ = 'vaughn'

import pytest
from . import TESTS_DATA


@pytest.mark.smoketest
def test_import_module():
    import agavepy


@pytest.mark.smoketest
def test_import_classes():
    from agavepy.agave import Agave, AgaveError, AgaveException


@pytest.mark.smoketest
def test_import_subs():
    from agavepy import tenants
    from agavepy import swaggerpy
    from agavepy import settings


@pytest.mark.smoketest
def test_temp_dir(temp_dir):
    t = temp_dir
    assert t.endswith('-tests')


@pytest.mark.smoketest
def test_temp_cache(temp_cache_env):
    t = temp_cache_env
    assert t.endswith('-cache')


def test_swaggerpy_client_log_level(tapis_py_log_level_debug):
    from agavepy import swaggerpy
    assert swaggerpy.client.LOG_LEVEL != None


def test_swaggerpy_log_level_env(tapis_py_log_level_debug):
    import os
    from agavepy import settings
    assert settings.TAPISPY_LOG_LEVEL == 'WARNING'
