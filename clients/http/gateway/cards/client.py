from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CardDict(TypedDict):
    """
    Card data structure.
    """
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str


class IssueVirtualCardRequestDict(TypedDict):
    """
    Data structure to issue a new virtual card
    """
    userId: str
    accountId: str


class IssueVirtualCardResponseDict(TypedDict):
    """
    Issue a new virtual card response structure.
    """
    card: CardDict


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Data structure to issue a new physical card
    """
    userId: str
    accountId: str


class IssuePhysicalCardResponseDict(TypedDict):
    """
    Issue a new physical card response structure.
    """
    card: CardDict


class CardsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with http-gateway /api/v1/cards service.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Issues a virtual card.

        :param request: Dict with data for a new virtual card.
        :return: Response object with response data.
        """
        return self.post(f'/api/v1/cards/issue-virtual-card', json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Issues a physical card.

        :param request: Dict with data for a new physical card.
        :return: Response object with response data.
        """
        return self.post('/api/v1/cards/issue-physical-card', json=request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseDict:
        request = IssueVirtualCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_virtual_card_api(request)
        return response.json()

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseDict:
        request = IssuePhysicalCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_physical_card_api(request)
        return response.json()


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Creates CardsGatewayHTTPClient instance.
    :return: ready-to-use CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client = build_gateway_http_client())
