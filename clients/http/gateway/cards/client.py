from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class IssueCardRequestDict(TypedDict):
    """
    Data structure to issue a new card
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with http-gateway /api/v1/cards service.
    """

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Issues a virtual card.

        :param request: Dict with data for a new virtual card.
        :return: Response object with response data.
        """
        return self.post(f'/api/v1/cards/issue-virtual-card', json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Issues a physical card.

        :param request: Dict with data for a new physical card.
        :return: Response object with response data.
        """
        return self.post('/api/v1/cards/issue-physical-card', json=request)


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Creates CardsGatewayHTTPClient instance.
    :return: ready-to-use CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client = build_gateway_http_client())
