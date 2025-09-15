from locust import User, between, task

from clients.grpc.gateway.locust import GatewayGRPCTaskSet


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    user_id: str | None = None

    @task(2)
    def create_user(self):
        create_user_response = self.users_gateway_client.create_user()
        self.user_id = create_user_response.user.id

    @task(2)
    def open_deposit_account(self):
        if not self.user_id:
            return

        self.accounts_gateway_client.open_deposit_account(user_id=self.user_id)

    @task(6)
    def get_accounts(self):
        if not self.user_id:
            return

        self.accounts_gateway_client.get_accounts(user_id=self.user_id)


class GetAccountsUser(User):
    host = 'localhost'
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)
