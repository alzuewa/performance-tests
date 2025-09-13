from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest,
    GetContractDocumentResponse
)
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest,
    GetTariffDocumentResponse
)


class DocumentsGatewayGRPCClient(GRPCClient):
    """
    gRPC-client to communicate with DocumentsGatewayService.
    Provides high-level methods to get documents.
    """

    def __init__(self, channel: Channel):
        super().__init__(channel)
        self.stub = DocumentsGatewayServiceStub(channel)

    def get_tariff_document_api(self, request: GetTariffDocumentRequest) -> GetTariffDocumentResponse:
        """
        Low-level GetTariffDocument method call via gRPC.

        :param request: gRPC-request with user ID.
        :return: Response from the service with tariff document data.
        """
        return self.stub.GetTariffDocument(request)

    def get_contract_document_api(self, request: GetContractDocumentRequest) -> GetContractDocumentResponse:
        """
        Low-level GetContractDocument method call via gRPC.

        :param request: gRPC-request with user ID.
        :return: Response from the service with contract document data.
        """
        return self.stub.GetContractDocument(request)

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponse:
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponse:
        request = GetContractDocumentRequest(account_id=account_id)
        return self.get_contract_document_api(request)


def build_documents_gateway_grpc_client() -> DocumentsGatewayGRPCClient:
    """
     factory method to get an instance of DocumentsGatewayGRPCClient.

    :return: Initialized client for DocumentsGatewayService.
    """
    return DocumentsGatewayGRPCClient(channel=build_gateway_grpc_client())

def build_documents_gateway_locust_grpc_client(environment: Environment) -> DocumentsGatewayGRPCClient:
    """
    Function to get an instance of DocumentsGatewayGRPCClient adapted for Locust.

    Client automatically collects metrics and passes it to Locust by the means of hooks.
    Is used exceptionally for load testing.

    :param environment: Locust environment object.
    :return: ready-to-use DocumentsGatewayGRPCClient with hooks to collect metrics.
    """
    return DocumentsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))
