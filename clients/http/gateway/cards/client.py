from httpx import Response
from locust.env import Environment

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.cards.schema import (
    IssuePhysicalCardRequestSchema,
    IssuePhysicalCardResponseSchema,
    IssueVirtualCardRequestSchema,
    IssueVirtualCardResponseSchema
)

class CardsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with http-gateway /api/v1/cards service.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestSchema) -> Response:
        """
        Issues a virtual card.

        :param request: Pydantic-model with data for a new virtual card.
        :return: Response object with response data.
        """
        return self.post(f'/api/v1/cards/issue-virtual-card', json=request.model_dump(by_alias=True))

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestSchema) -> Response:
        """
        Issues a physical card.

        :param request: Pydantic-model with data for a new physical card.
        :return: Response object with response data.
        """
        return self.post('/api/v1/cards/issue-physical-card', json=request.model_dump(by_alias=True))

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        request = IssueVirtualCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request)
        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        request = IssuePhysicalCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Creates CardsGatewayHTTPClient instance.
    :return: ready-to-use CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client = build_gateway_http_client())

def build_cards_gateway_locust_http_client(environment: Environment) -> CardsGatewayHTTPClient:
    """
    Creates CardsGatewayHTTPClient adapted for Locust.

    Client automatically collects metrics and passes it to Locust by the means of hooks.
    Is used exceptionally for load testing.

    :param environment: Locust environment object.
    :return: ready-to-use CardsGatewayHTTPClient with hooks to collect metrics.
    """
    return CardsGatewayHTTPClient(client = build_gateway_locust_http_client(environment))