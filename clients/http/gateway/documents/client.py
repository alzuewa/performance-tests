from httpx import Response
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.documents.schema import GetContractDocResponseSchema, GetTariffDocResponseSchema


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with http-gateway /api/v1/documents service.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Gets the tariff of the account.

        :param account_id: id of the account.
        :return: Response object with response data.
        """
        return self.get(
            f'/api/v1/documents/tariff-document/{account_id}',
            extensions=HTTPClientExtensions(route='/api/v1/documents/tariff-document/{account_id}')
        )

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Gets the contract of the account.

        :param account_id: id of the account.
        :return: Response object with response data.
        """
        return self.get(
            f'/api/v1/documents/contract-document/{account_id}',
            extensions=HTTPClientExtensions(route='/api/v1/documents/contract-document/{account_id}')
        )

    def get_tariff_document(self, account_id: str) -> GetTariffDocResponseSchema:
        response = self.get_tariff_document_api(account_id)
        return GetTariffDocResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocResponseSchema:
        response = self.get_contract_document_api(account_id)
        return GetContractDocResponseSchema.model_validate_json(response.text)


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Creates DocumentsGatewayHTTPClient instance.
    :return: ready-to-use DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())


def build_documents_gateway_locust_http_client(environment: Environment) -> DocumentsGatewayHTTPClient:
    """
    Creates DocumentsGatewayHTTPClient adapted for Locust.

    Client automatically collects metrics and passes it to Locust by the means of hooks.
    Is used exceptionally for load testing.

    :param environment: Locust environment object.
    :return: ready-to-use DocumentsGatewayHTTPClient with hooks to collect metrics.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))
