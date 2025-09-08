from typing import Any

from httpx import Client, QueryParams, Response, URL


class HTTPClient:
    """
    Base HTTP API client, takes httpx.Client.

    :param client: httpx.Client instance to make HTTP-requests
    """

    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Performs a GET-request.

        :param url: endpoint URL.
        :param params: request query params (i.e., ?key=value).
        :return: Response object with response data.
        """
        return self.client.get(url=url, params=params)

    def post(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Performs a POST-request.

        :param url: endpoint URL.
        :param json: request JSON-data.
        :return: Response object with response data.
        """
        return self.client.post(url=url, json=json)
