"""Read from tests/configuration.json or environment vars
"""
import json
import os
import pytest

from agavepy.constants import DEFAULT_TENANT_ID, DEFAULT_TENANT_API_SERVER

PWD = os.getcwd()
HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
GPARENT = os.path.dirname(PARENT)
CREDENTIALS = os.path.join(PARENT, 'configuration.json')

ENV_KEY_MAP = [('TEST_TAPIS_API_KEY', 'apikey', None),
               ('TEST_TAPIS_API_SECRET', 'apisecret', None),
               ('TEST_TAPIS_USERNAME', 'username', None),
               ('TEST_TAPIS_PASSWORD', 'password', None),
               ('TEST_TAPIS_BASE_URL', 'apiserver', DEFAULT_TENANT_API_SERVER),
               ('TEST_TAPIS_TENANT_ID', 'tenantid', DEFAULT_TENANT_ID),
               ('TEST_TAPIS_TOKEN', 'token', None),
               ('TEST_TAPIS_REFRESH_TOKEN', 'refresh_token', None),
               ('TEST_TAPIS_VERIFY_CERTS', 'verify_certs', True),
               ('TEST_TAPIS_CLIENT_NAME', 'client_name', None)]


@pytest.fixture(scope='session')
def credentials(filename=CREDENTIALS):
    try:
        creds = json.load(open(filename, 'r'))
    except Exception:
        creds = dict()
    client = dict()
    for e, k, d in ENV_KEY_MAP:
        client[k] = creds.get(k, os.environ.get(e, d))
    return client


@pytest.fixture(scope='session')
def test_username(credentials):
    return credentials.get('username')


@pytest.fixture(scope='session')
def test_password(credentials):
    return credentials.get('password')


@pytest.fixture(scope='session')
def test_tenant_id(credentials):
    return credentials.get('tenantid')


@pytest.fixture(scope='session')
def test_api_key(credentials):
    return credentials.get('apikey')


@pytest.fixture(scope='session')
def test_api_secret(credentials):
    return credentials.get('apisecret')


@pytest.fixture(scope='session')
def test_api_server(credentials):
    return credentials.get('apiserver')


@pytest.fixture(scope='session')
def test_forever_token(credentials):
    return credentials.get('token')


@pytest.fixture(scope='function')
def test_client(test_api_key, test_api_secret, test_username, test_password,
                test_tenant_id, test_api_server):
    return {
        'TAPIS_API_KEY': test_api_key,
        'TAPIS_API_SECRET': test_api_secret,
        'TAPIS_USERNAME': test_username,
        'TAPIS_PASSWORD': test_password,
        'TAPIS_TENANT_ID': test_tenant_id,
        'TAPIS_BASE_URL': test_api_server
    }


@pytest.fixture(scope='function')
def bare_client(test_api_server, test_forever_token):
    return {
        'TAPIS_BASE_URL': test_api_server,
        'TAPIS_TOKEN': test_forever_token
    }


@pytest.fixture(scope='function')
def basic_client(test_username, test_password, test_api_server):
    return {
        'TAPIS_USERNAME': test_username,
        'TAPIS_PASSWORD': test_password,
        'TAPIS_BASE_URL': test_api_server
    }


@pytest.fixture(scope='function')
def incomplete_client(test_api_server, test_username):
    return {'TAPIS_BASE_URL': test_api_server, 'TAPIS_USERNAME': test_username}


@pytest.fixture(scope='function')
def token_only_client(test_api_server, test_forever_token):
    return {
        'TAPIS_BASE_URL': test_api_server,
        'TAPIS_TOKEN': test_forever_token
    }


@pytest.fixture(scope='function')
def temp_cache_env(temp_cache, monkeypatch):
    """Set credentials cache to a temp directory
    """
    monkeypatch.setenv('TAPIS_CACHE_DIR', temp_cache)
    return temp_cache


@pytest.fixture(scope='function')
def temp_cache_b_env(temp_cache_b, monkeypatch):
    """Set credentials cache to a temp directory
    """
    monkeypatch.setenv('TAPIS_CACHE_DIR', temp_cache_b)
    return temp_cache_b


@pytest.fixture(scope='function')
def temp_testing_env(test_client, temp_cache_env, monkeypatch):
    """Configure client with test credentials and temp dir
    """
    for k, v in test_client.items():
        monkeypatch.setenv(k, v)


@pytest.fixture(scope='function')
def bare_testing_env(bare_client, temp_cache_env, monkeypatch):
    """Configure client with test credentials and temp dir
    """
    for k, v in bare_client.items():
        monkeypatch.setenv(k, v)


@pytest.fixture(scope='function')
def basic_testing_env(basic_client, temp_cache_env, monkeypatch):
    """Configure client with test credentials and temp dir
    """
    for k, v in basic_client.items():
        monkeypatch.setenv(k, v)


@pytest.fixture(scope='function')
def incomplete_testing_env(incomplete_client, temp_cache_env, monkeypatch):
    """Configure client with test credentials and temp dir
    """
    for k, v in incomplete_client.items():
        monkeypatch.setenv(k, v)


@pytest.fixture(scope='function')
def temp_cache_empty_env(temp_cache_empty, monkeypatch):
    """Set credentials cache to a temp directory
    """
    monkeypatch.setenv('TAPIS_CACHE_DIR', temp_cache_empty)
    return temp_cache_empty


@pytest.fixture(scope='function')
def tapis_py_log_level_debug(monkeypatch):
    monkeypatch.setenv('TAPISPY_LOG_LEVEL', 'DEBUG')
    monkeypatch.setenv('SWAGGERPY_LOG_LEVEL', 'WARNING')
    return 'DEBUG'
