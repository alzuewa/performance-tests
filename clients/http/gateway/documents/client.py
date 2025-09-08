from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


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
        return self.get(f'/api/v1/documents/tariff-document/{account_id}')

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Gets the contract of the account.

        :param account_id: id of the account.
        :return: Response object with response data.
        """
        return self.get(f'/api/v1/documents/contract-document/{account_id}')


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Creates DocumentsGatewayHTTPClient instance.
    :return: ready-to-use DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client = build_gateway_http_client())
