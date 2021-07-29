from .client import Client


class Talk(Client):
    def __init__(self) -> None:
        pass

    def exec(self):
        self._request()
