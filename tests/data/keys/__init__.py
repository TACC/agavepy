import base64
import os

HERE = os.path.abspath(__file__)
PARENT = os.path.dirname(HERE)

__all__ = [
    'test_pem_path', 'test_pub_path', 'test_piv_path', 'b64encode',
    'b64decode', 'pubkey_from_file', 'privkey_from_file'
]


def test_pem_path():
    return os.path.join(PARENT, 'tapis-testing.pem')


def test_priv_path():
    return os.path.join(PARENT, 'tapis-testing')


def test_pub_path():
    return os.path.join(PARENT, 'tapis-testing.pub')


def b64encode(data):
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr


def b64decode(b64data):
    return str(base64.b64decode(b64data).decode('utf-8'))


def pubkey_from_file():
    with open(test_pub_path(), 'r') as pub:
        return pub.read()


def privkey_from_file():
    with open(test_priv_path(), 'r') as prv:
        return prv.read()
