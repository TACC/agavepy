import pytest
from . import TESTS_DATA


@pytest.mark.smoketest
def test_client_read_env(temp_testing_env, test_client):
    """Can read client config from ENV
    """
    from agavepy.agave import Agave
    client = Agave._read_env()
    assert client['username'] == test_client['TAPIS_USERNAME']


@pytest.mark.smoketest
def test_client_current_agpy(temp_testing_env):
    """Legacy and current cache paths both resolve
    """
    from agavepy.agave import Agave
    assert Agave.agpy_path() == Agave.tapis_current_path()


@pytest.mark.smoketest
def test_restore_client_env(temp_testing_env, test_username):
    """Can restore client from environment
    """
    from agavepy.agave import Agave
    client = Agave.restore()
    assert client.username == test_username


@pytest.mark.smoketest
def test_read_sessions(temp_testing_env, test_username, test_tenant_id,
                       test_api_key):
    """Can read sessions from file
    """
    from agavepy.agave import Agave
    client = Agave.restore()
    s = client._read_sessions()
    assert 'sessions' in s
    assert test_tenant_id in s['sessions']
    assert test_username in s['sessions'][test_tenant_id]
    assert test_api_key in s['sessions'][test_tenant_id][test_username]


@pytest.mark.smoketest
def test_client_from_inited_file(test_username, temp_cache, temp_cache_b_env):
    """Can load client bootstrapped entirely from a cache file
    """
    import os
    import shutil
    from agavepy.agave import Agave
    # Assumption:
    # A test has been run that populates temp_cache
    # TODO - model this as an explicit dependency
    shutil.copy(os.path.join(temp_cache, 'current'),
                os.path.join(temp_cache_b_env, 'current'))
    client = Agave.restore()
    discovered_cache_dir = os.path.basename(
        os.path.dirname(Agave.tapis_current_path()))
    configured_cache_dir = os.path.basename(temp_cache_b_env)

    assert os.path.basename(temp_cache) != configured_cache_dir
    assert os.path.basename(temp_cache) != discovered_cache_dir
    assert configured_cache_dir == discovered_cache_dir
    assert client.username == test_username


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
    with pytest.raises(FileNotFoundError):
        Agave.restore()

@pytest.mark.smoketest
def test_token_only_client(temp_testing_env, test_api_server, test_forever_token, test_username):
    """Client can make API call using only server and token
    """
    from agavepy.agave import Agave
    ag = Agave(api_server=test_api_server, token=test_forever_token)
    assert 'username' in ag.profiles.listByUsername(username=test_username)    

def test_token_only_client_refresh(temp_testing_env, test_api_server, test_forever_token):
    """Client.refresh() does not fail for token-only client
    """
    from agavepy.agave import Agave
    ag = Agave(api_server=test_api_server, token=test_forever_token)
    assert ag.refresh() == test_forever_token

def test_token_only_client_restore(temp_cache_empty_env, test_api_server, test_forever_token):
    """Client.restore() allowed even in token-only mode
    """
    from agavepy.agave import Agave
    ag = Agave(api_server=test_api_server, token=test_forever_token)
    ag.restore()

def test_token_only_client_no_write_cache(temp_testing_env, test_api_server, test_forever_token):
    """Client.refresh() does not fail for token-only client
    """
    from agavepy.agave import Agave
    ag = Agave(api_server=test_api_server, token=test_forever_token)
    with pytest.raises(NotImplementedError):
        ag._write_client()

