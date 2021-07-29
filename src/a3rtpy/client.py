import urllib.request


class Client:
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def _request(self, endpoint: str, params: dict, method: str):
        print("urllib.request", urllib.request)
