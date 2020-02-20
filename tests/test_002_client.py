__author__ = 'vaughn'

import pytest
from . import TESTS_DATA

# Special case - bare client


@pytest.mark.smoketest
def test_client_restore_direct(bare_testing_env, test_api_server,
                               test_forever_token):
    """Can init bare client config from params
    """
    from agavepy.agave import Agave
    client = Agave._restore_direct(api_server=test_api_server,
                                   token=test_forever_token)
    assert client.profiles.get() is not None


@pytest.mark.smoketest
def test_client_restore_direct_env(bare_testing_env):
    """Can init bare client config from ENV
    """
    from agavepy.agave import Agave
    client = Agave._restore_direct()
    assert client.profiles.get() is not None


@pytest.mark.smoketest
def test_client_restore_direct_env_fail(incomplete_testing_env):
    """Bare client read fails on missing ENV variables
    """
    from agavepy.agave import Agave
    from agavepy.agave import AgaveError
    with pytest.raises(AgaveError):
        client = Agave._restore_direct()
        assert client.profiles.get() is not None


# From env


@pytest.mark.smoketest
def test_client_restore_env_refresh(temp_testing_env, test_client):
    """Can read refresh client config from ENV
    """
    from agavepy.agave import Agave
    client = Agave._restore_env()
    assert client.username == test_client['TAPIS_USERNAME']
    assert client.profiles.get() is not None


@pytest.mark.smoketest
def test_client_restore_env_basic(basic_testing_env, basic_client,
                                  test_username):
    """Can read basic client config from ENV
    """
    from agavepy.agave import Agave
    client = Agave._restore_env()
    assert client.api_server == basic_client['TAPIS_BASE_URL']
    assert client.username == test_username


@pytest.mark.smoketest
def test_client_restore_env_bare(bare_testing_env, bare_client):
    """Can read bare client config from ENV
    """
    from agavepy.agave import Agave
    client = Agave._restore_env()
    assert client.profiles.get() is not None


@pytest.mark.smoketest
def test_client_restore_env_incomplete(incomplete_testing_env):
    """Client read fails on missing ENV variables
    """
    from agavepy import Agave
    from agavepy.agave import AgaveError
    with pytest.raises(AgaveError):
        Agave._restore_env()


# Cached credentials


@pytest.mark.smoketest
def test_client_current_agpy(temp_testing_env):
    """Legacy and current cache path functions mutually, identically resolve
    """
    from agavepy.agave import Agave
    assert Agave.agpy_path() == Agave.tapis_current_path()


@pytest.mark.smoketest
def test_client_restore_generic(temp_testing_env, test_client,
                                tapis_py_log_level_debug):
    """Can read refresh client config from ENV
    """
    from agavepy.agave import Agave
    client = Agave.restore()
    assert client.username == test_client['TAPIS_USERNAME']
    assert client.profiles.get() is not None


@pytest.mark.smoketest
def test_profiles_api(temp_testing_env, test_username):
    from agavepy.agave import Agave
    client = Agave.restore()
    assert 'username' in client.profiles.listByUsername(username=test_username)


@pytest.mark.smoketest
def test_empty_cachedir_fail(temp_cache_empty_env):
    """Empty cache directory causes restore() to fail
    """
    from agavepy.agave import Agave
    from agavepy.agave import AgaveError
    with pytest.raises(AgaveError):
        Agave.restore()


@pytest.mark.smoketest
def test_bare_client_param(temp_testing_env, test_api_server,
                           test_forever_token, test_username,
                           tapis_py_log_level_debug):
    """Client can make API call using only server and token
    """
    from agavepy.agave import Agave
    ag = Agave(api_server=test_api_server, token=test_forever_token)
    assert 'username' in ag.profiles.listByUsername(username=test_username)


def test_bare_client_param_refresh(temp_testing_env, test_api_server,
                                   test_forever_token):
    """Client.refresh() does not fail for token-only client
    """
    from agavepy.agave import Agave
    ag = Agave(api_server=test_api_server, token=test_forever_token)
    assert ag.refresh() == test_forever_token


def test_bare_client_env_restore(bare_testing_env, test_api_server,
                                 test_forever_token):
    """Client.restore() allowed even in token-only mode
    """
    from agavepy.agave import Agave
    from agavepy.agave import AgaveError
    ag = Agave(api_server=test_api_server, token=test_forever_token)
    ag.restore()
    assert ag.profiles.get() is not None
    ah = Agave.restore()
    assert ah.profiles.get() is not None


def test_bare_client_no_write_cache(temp_testing_env, test_api_server,
                                    test_forever_token):
    """Client.refresh() does not fail for token-only client
    """
    from agavepy.agave import Agave
    ag = Agave(api_server=test_api_server, token=test_forever_token)
    with pytest.raises(NotImplementedError):
        ag._write_client(permissive=False)
