# from a3rtpy import client
# from a3rtpy import __version__
# import pytest

# import pytest

# import a3rtpy
from a3rtpy.talk import Talk

# class Client(object):
#     def send(self, msg):
#         # ...
#         pass


# @pytest.fixture()
# def client():
#     return Client("connect info")


# def test_sample(client):
#     client.send("message")


# @pytest.fixture()
def test_talk_success():
    # mocker
    # talk = a3rtpy.talk.Talk()
    # talk.exec()

    print("a3rtpy", Talk)

    assert 1 == 1
