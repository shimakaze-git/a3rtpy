# from a3rtpy import client
# from a3rtpy import __version__
# import pytest

import pytest
import a3rtpy


class Client(object):
    def send(self, msg):
        # ...
        pass


@pytest.fixture()
def client():
    return Client("connect info")


def test_sample(client):
    client.send("message")


def test_create_default_client():
    client = a3rtpy.client()
    assert client == {}
