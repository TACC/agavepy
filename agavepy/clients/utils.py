import petname
import socket


def random_client_name(words=3, letters=6, hostname=False):
    client_name = petname.generate(words=words, letters=letters)
    if hostname:
        client_name = socket.gethostname().lower() + '-' + client_name
    return client_name
