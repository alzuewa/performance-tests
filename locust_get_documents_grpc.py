from locust import User, between, task

from clients.grpc.gateway.locust import GatewayGRPCSequentialTaskSet
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import OpenSavingsAccountResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetDocumentsSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    """
    Load test scenario which sequentially does the following:
    1. Creates a new user.
    2. Opens a savings account.
    3. Get account documents (tariff and contract).

    Uses base GatewayGRPCSequentialTaskSet and API-clients created there.
    """

    # Shared state — save requests' results for further usage
    create_user_response: CreateUserResponse | None = None
    open_savings_account_response: OpenSavingsAccountResponse | None = None

    @task
    def create_user(self):
        """
        Create a new user and save request result for its using in the next steps.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_savings_account(self):
        """
        Open a savings account for previously created user.
        Check that the previous step was successful.
        """
        # there may be an unexpected case when a user is not created for some reason
        if not self.create_user_response:
            return

        self.open_savings_account_response = self.accounts_gateway_client.open_savings_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def get_documents(self):
        """
        Get documents if the account was successfully created.
        """
        # there may be an unexpected case when an account is not created for some reason
        if not self.open_savings_account_response:
            return

        self.documents_gateway_client.get_tariff_document(
            account_id=self.open_savings_account_response.account.id
        )
        self.documents_gateway_client.get_contract_document(
            account_id=self.open_savings_account_response.account.id
        )


class GetDocumentsUser(User):
    """
    Locust User instance executing a scenario of getting documents by sequentially ordered steps.
    """
    host = 'localhost'
    tasks = [GetDocumentsSequentialTaskSet]
    wait_time = between(1, 3)
