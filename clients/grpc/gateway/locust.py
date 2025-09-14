from locust import SequentialTaskSet, TaskSet

from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client
from clients.grpc.gateway.cards.client import CardsGatewayGRPCClient, build_cards_gateway_locust_grpc_client
from clients.grpc.gateway.documents.client import DocumentsGatewayGRPCClient, build_documents_gateway_locust_grpc_client
from clients.grpc.gateway.operations.client import OperationsGatewayGRPCClient, build_operations_gateway_locust_grpc_client
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client


class GatewayGRPCTaskSet(TaskSet):
    """
    Base TaskSet for grpc-gateway scenarios. The order of tasks execution is not important.
    """

    # Clients itself are initialized after on_start() is called
    users_gateway_client: UsersGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    documents_gateway_client: DocumentsGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient

    def on_start(self) -> None:
        """
        The method is called before TaskSet is executed.
        """
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_grpc_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_grpc_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_grpc_client(self.user.environment)


class GatewayGRPCSequentialTaskSet(SequentialTaskSet):
    """
    Base SequentialTaskSet for grpc-gateway scenarios where the tasks have to be executed within a strictly defined order.
    """

    users_gateway_client: UsersGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    documents_gateway_client: DocumentsGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient

    def on_start(self) -> None:
        """
        The method is called before TaskSet is executed.
        """
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_grpc_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_grpc_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_grpc_client(self.user.environment)
