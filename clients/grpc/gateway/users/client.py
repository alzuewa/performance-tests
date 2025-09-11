from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from tools.fakers import fake


class UsersGatewayGRPCClient(GRPCClient):
    """
    gRPC-client to communicate with UsersGatewayService.
    Provides high-level methods to get and create users.
    """

    def __init__(self, channel: Channel):
        super().__init__(channel)
        self.stub = UsersGatewayServiceStub(channel)  # gRPC-stub generated from .proto

    def get_user_api(self, request: GetUserRequest) -> GetUserResponse:
        """
        Low-level GetUser method call via gRPC.

        :param request: gRPC-request with user ID.
        :return: Response from the service with user data.
        """
        return self.stub.GetUser(request)

    def create_user_api(self, request: CreateUserRequest) -> CreateUserResponse:
        """
        Low-level CreateUser method call via gRPC.

        :param request: gRPC-request with a new user data.
        :return: Response from the service with created user data.
        """
        return self.stub.CreateUser(request)

    def get_user(self, user_id: str) -> GetUserResponse:
        """
        Gets user data by user ID.

        :param user_id: ID of the user.
        :return: Response with user data.
        """
        request = GetUserRequest(id=user_id)
        return self.get_user_api(request)

    def create_user(self) -> CreateUserResponse:
        """
        Creates a new user with fake data.

        :return: Response with newly created user data.
        """
        request = CreateUserRequest(
            email=fake.email(),
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            middle_name=fake.middle_name(),
            phone_number=fake.phone_number()
        )
        return self.create_user_api(request)


def build_users_gateway_grpc_client() -> UsersGatewayGRPCClient:
    """
    A factory method to get an instance of UsersGatewayGRPCClient.

    :return: Initialized client for UsersGatewayService.
    """
    return UsersGatewayGRPCClient(channel=build_gateway_grpc_client())
