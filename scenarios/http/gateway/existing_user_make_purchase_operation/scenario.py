from locust import events, task
from locust.env import Environment

from clients.http.gateway.locust import GatewayHTTPTaskSet
from seeds.scenarios.existing_user_make_purchase_operation import ExistingUserMakePurchaseOperationSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


# Initialization hook — is invoked before load test scenario starts
@events.init.add_listener
def init(environment: Environment, **kwargs):
    # Execute seeding scenario
    seeds_scenario = ExistingUserMakePurchaseOperationSeedsScenario()
    seeds_scenario.build()  # create users, accounts, cards, and operations

    # Load seeding result from the saved JSON-file
    environment.seed_result = seeds_scenario.load()


# TaskSet — user scenario. Each virtual user executes these tasks
class MakePurchaseOperationTaskSet(GatewayHTTPTaskSet):
    seed_user: SeedUserResult

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seed_result.get_random_user()

    @task(1)
    def make_purchase_operation(self):
        self.operations_gateway_client.make_purchase_operation(
            card_id=self.seed_user.credit_card_accounts[0].physical_cards[0].card_id,
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    @task(2)
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(2)
    def get_operations(self):
        self.operations_gateway_client.get_operations(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    @task(2)
    def get_operations_summary(self):
        self.operations_gateway_client.get_operations_summary(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )


# Client class invoking the TaskSet
class MakePurchaseOperationScenarioUser(LocustBaseUser):
    tasks = [MakePurchaseOperationTaskSet]
