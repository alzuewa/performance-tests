from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import GetAccountsRequest, GetAccountsResponse
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import (
    OpenDepositAccountRequest,
    OpenDepositAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import (
    OpenSavingsAccountRequest,
    OpenSavingsAccountResponse
)


class AccountsGatewayGRPCClient(GRPCClient):
    """
    gRPC-client to communicate with AccountsGatewayService.
    Provides high-level methods to get and create accounts.
    """

    def __init__(self, channel: Channel):
        super().__init__(channel)
        self.stub = AccountsGatewayServiceStub(channel)

    def get_accounts_api(self, request: GetAccountsRequest) -> GetAccountsResponse:
        """
        Low-level GetAccounts method call via gRPC.

        :param request: gRPC-request with user ID.
        :return: Response from the service with user accounts data.
        """
        return self.stub.GetAccounts(request)

    def open_deposit_account_api(self, request: OpenDepositAccountRequest) -> OpenDepositAccountResponse:
        """
        Low-level OpenDepositAccount method call via gRPC.

        :param request: gRPC-request with user ID.
        :return: Response from the service with opened deposit account data.
        """
        return self.stub.OpenDepositAccount(request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequest) -> OpenSavingsAccountResponse:
        """
        Low-level OpenSavingsAccount method call via gRPC.

        :param request: gRPC-request with user ID.
        :return: Response from the service with opened savings account data.
        """
        return self.stub.OpenSavingsAccount(request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequest) -> OpenDebitCardAccountResponse:
        """
        Low-level OpenDebitCardAccount method call via gRPC.

        :param request: gRPC-request with user ID.
        :return: Response from the service with opened debit account data.
        """
        return self.stub.OpenDebitCardAccount(request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequest) -> OpenCreditCardAccountResponse:
        """
        Low-level OpenCreditCardAccount method call via gRPC.

        :param request: gRPC-request with user ID.
        :return: Response from the service with opened credit account data.
        """
        return self.stub.OpenCreditCardAccount(request)

    def get_accounts(self, user_id: str) -> GetAccountsResponse:
        request = GetAccountsRequest(user_id=user_id)
        return self.get_accounts_api(request)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponse:
        request = OpenDepositAccountRequest(user_id=user_id)
        return self.open_deposit_account_api(request)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponse:
        request = OpenSavingsAccountRequest(user_id=user_id)
        return self.open_savings_account_api(request)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponse:
        request = OpenDebitCardAccountRequest(user_id=user_id)
        return self.open_debit_card_account_api(request)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponse:
        request = OpenCreditCardAccountRequest(user_id=user_id)
        return self.open_credit_card_account_api(request)


def build_accounts_gateway_grpc_client() -> AccountsGatewayGRPCClient:
    """
    A factory method to get an instance of AccountsGatewayGRPCClient.

    :return: Initialized client for AccountsGatewayGRPCClient.
    """
    return AccountsGatewayGRPCClient(channel=build_gateway_grpc_client())


def build_accounts_gateway_locust_grpc_client(environment: Environment) -> AccountsGatewayGRPCClient:
    """
    Function to get an instance of AccountsGatewayGRPCClient adapted for Locust.

    Client automatically collects metrics and passes it to Locust by the means of hooks.
    Is used exceptionally for load testing.

    :param environment: Locust environment object.
    :return: ready-to-use AccountsGatewayGRPCClient with hooks to collect metrics.
    """
    return AccountsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))
