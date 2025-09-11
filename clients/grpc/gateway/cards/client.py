from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import IssueVirtualCardRequest, IssueVirtualCardResponse
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardRequest, IssuePhysicalCardResponse
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub
from tools.fakers import fake


class CardsGatewayGRPCClient(GRPCClient):
    """
    gRPC-client to communicate with CardsGatewayService.
    Provides high-level methods to issue cards.
    """

    def __init__(self, channel: Channel):
        super().__init__(channel)
        self.stub = CardsGatewayServiceStub(channel)  # gRPC-stub generated from .proto

    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> IssueVirtualCardResponse:
        """
        Low-level IssueVirtualCard method call via gRPC.

        :param request: gRPC-request with user ID and account ID.
        :return: Response from the service with card data.
        """
        return self.stub.IssueVirtualCard(request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        """
        Low-level IssuePhysicalCard method call via gRPC.

        :param request: gRPC-request with user ID and account ID
        :return: Response from the service with card data.
        """
        return self.stub.IssuePhysicalCard(request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponse:
        """
        Issues a new virtual card.

        :param user_id: ID of the user.
        :param account_id: ID of the account.
        :return: Response with card data.
        """
        request = IssueVirtualCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_virtual_card_api(request)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        """
        Issues a new physical card.

        :param user_id: ID of the user.
        :param account_id: ID of the account.
        :return: Response with card data.
        """
        request = IssuePhysicalCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_physical_card_api(request)


def build_cards_gateway_grpc_client() -> CardsGatewayGRPCClient:
    """
    A factory method to get an instance of CardsGatewayGRPCClient.

    :return: Initialized client for CardsGatewayService.
    """
    return CardsGatewayGRPCClient(channel=build_gateway_grpc_client())
