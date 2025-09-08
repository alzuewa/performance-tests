from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class TariffDict(TypedDict):
    """
    Tariff data structure.
    """
    url: str
    document: str


class GetTariffDocResponseDict(TypedDict):
    """
    Get tariff document response data structure.
    """
    tariff: TariffDict


class ContractDict(TypedDict):
    """
    Contract data structure.
    """
    url: str
    document: str


class GetContractDocResponseDict(TypedDict):
    """
    Get contract document response data structure.
    """
    tariff: ContractDict


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

    def get_tariff_document(self, account_id: str) -> GetTariffDocResponseDict:
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocResponseDict:
        response = self.get_contract_document_api(account_id)
        return response.json()

def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Creates DocumentsGatewayHTTPClient instance.
    :return: ready-to-use DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client = build_gateway_http_client())
