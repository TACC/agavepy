import os
import pytest
from tempfile import mkdtemp

__all__ = ['temp_dir', 'temp_cache', 'temp_cache_b', 'temp_cache_empty']


@pytest.fixture(scope='session')
def temp_dir():
    """Alternative to pytest's temporary directory function
    """
    return mkdtemp(prefix='tapispy-', suffix='-tests')


@pytest.fixture(scope='session')
def temp_cache():
    """Alternative to pytest's temporary directory function
    """
    return mkdtemp(prefix='tapispy-', suffix='-cache')


@pytest.fixture(scope='session')
def temp_cache_b():
    """Alternative to pytest's temporary directory function
    """
    return mkdtemp(prefix='tapispy-', suffix='-cache_b')


@pytest.fixture(scope='session')
def temp_cache_empty():
    """Alternative to pytest's temporary directory function
    """
    return mkdtemp(prefix='tapispy-', suffix='-cache_e')
