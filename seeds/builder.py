from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client, AccountsGatewayGRPCClient
from clients.grpc.gateway.cards.client import build_cards_gateway_grpc_client, CardsGatewayGRPCClient
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client, OperationsGatewayGRPCClient
from clients.grpc.gateway.users.client import build_users_gateway_grpc_client, UsersGatewayGRPCClient
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client, AccountsGatewayHTTPClient
from clients.http.gateway.cards.client import build_cards_gateway_http_client, CardsGatewayHTTPClient
from clients.http.gateway.operations.client import build_operations_gateway_http_client, OperationsGatewayHTTPClient
from clients.http.gateway.users.client import build_users_gateway_http_client, UsersGatewayHTTPClient
from seeds.schema.plan import (
    SeedsPlan,
    SeedUsersPlan,
    SeedAccountsPlan,
)
from seeds.schema.result import (
    SeedsResult,
    SeedUserResult,
    SeedCardResult,
    SeedAccountResult,
    SeedOperationResult
)


class SeedsBuilder:
    """
    SeedsBuilder — generator (seeder) creating test data based on passed Seeds Plan.
    Works with both HTTP and gRPC clients.

    Attributes:
        users_gateway_client: Users client (HTTP or gPRC).
        cards_gateway_client: Cards client.
        accounts_gateway_client: Accounts client.
        operations_gateway_client: Operations client (top-up, purchases, etc.).
    """

    def __init__(
            self,
            users_gateway_client: UsersGatewayGRPCClient | UsersGatewayHTTPClient,
            cards_gateway_client: CardsGatewayGRPCClient | CardsGatewayHTTPClient,
            accounts_gateway_client: AccountsGatewayGRPCClient | AccountsGatewayHTTPClient,
            operations_gateway_client: OperationsGatewayGRPCClient | OperationsGatewayHTTPClient
    ):
        self.users_gateway_client = users_gateway_client
        self.cards_gateway_client = cards_gateway_client
        self.accounts_gateway_client = accounts_gateway_client
        self.operations_gateway_client = operations_gateway_client

    def build_physical_card_result(self, user_id: str, account_id: str) -> SeedCardResult:
        """
        Issues a physical card for the passed user and account.

        Args:
            user_id: User ID.
            account_id: Account ID.

        Returns:
            SeedCardResult: Result with the ID of the issued physical card.
        """
        response = self.cards_gateway_client.issue_physical_card(
            user_id=user_id,
            account_id=account_id
        )
        return SeedCardResult(card_id=response.card.id)

    def build_virtual_card_result(self, user_id: str, account_id: str) -> SeedCardResult:
        """
        Issues a virtual card for the passed user and account.

        Args:
            user_id: User ID.
            account_id: Account ID.

        Returns:
            SeedCardResult: Result with the ID of the issued virtual card.
        """
        response = self.cards_gateway_client.issue_virtual_card(
            user_id=user_id,
            account_id=account_id
        )
        return SeedCardResult(card_id=response.card.id)

    def build_top_up_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Makes top-up operation on the card.

        Args:
            card_id: Card ID.
            account_id: Account ID.

        Returns:
            SeedOperationResult: Result with the ID of the performed top-up operation.
        """
        response = self.operations_gateway_client.make_top_up_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_purchase_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Makes purchase operation on the card.

        Args:
            card_id: Card ID.
            account_id: Account ID.

        Returns:
            SeedOperationResult: Result with the ID of the performed purchase operation.
        """
        response = self.operations_gateway_client.make_purchase_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_transfer_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Makes transfer operation on the card.

        Args:
            card_id: Card ID.
            account_id: Account ID.

        Returns:
            SeedOperationResult: Result with the ID of the performed transfer operation.
        """
        response = self.operations_gateway_client.make_transfer_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_cash_withdrawal_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Makes cash withdrawal operation on the card.

        Args:
            card_id: Card ID.
            account_id: Account ID.

        Returns:
            SeedOperationResult: Result with the ID of the performed cash withdrawal operation.
        """
        response = self.operations_gateway_client.make_cash_withdrawal_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_savings_account_result(self, user_id: str) -> SeedAccountResult:
        """
        Opens a savings account for the user.

        Args:
            user_id: User ID.

        Returns:
            SeedAccountResult: Result with the ID of the created account.
        """
        response = self.accounts_gateway_client.open_savings_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_deposit_account_result(self, user_id: str) -> SeedAccountResult:
        """
        Opens a deposit account for the user.

        Args:
            user_id: User ID.

        Returns:
            SeedAccountResult: Result with the ID of the created account.
        """
        response = self.accounts_gateway_client.open_deposit_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_debit_card_account_result(self, plan: SeedAccountsPlan, user_id: str) -> SeedAccountResult:
        """
        Opens a debit account for the user and optionally:
        - issues physical cards
        - issues virtual cards
        - makes top-up operations
        - makes purchase operations
        - makes transfer operations
        - makes cash withdrawal operations

        Args:
            plan: Debit account Seed Plan.
            user_id: User ID.

        Returns:
            SeedAccountResult: Result with the ID of the created account and additional options (cards, operations)
        """
        response = self.accounts_gateway_client.open_debit_card_account(user_id=user_id)
        card_id = response.account.cards[0].id
        account_id = response.account.id

        return SeedAccountResult(
            account_id=response.account.id,
            physical_cards=[
                self.build_physical_card_result(user_id=user_id, account_id=response.account.id)
                for _ in range(plan.physical_cards.count)
            ],
            virtual_cards=[
                self.build_virtual_card_result(user_id=user_id, account_id=response.account.id)
                for _ in range(plan.virtual_cards.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ],
            transfer_operations=[
                self.build_transfer_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ],
            cash_withdrawal_operations=[
                self.build_cash_withdrawal_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ],
        )

    def build_credit_card_account_result(self, plan: SeedAccountsPlan, user_id: str) -> SeedAccountResult:
        """
        Opens a credit account for the user and optionally:
        - issues physical cards
        - issues virtual cards
        - makes top-up operations
        - makes purchase operations
        - makes transfer operations
        - makes cash withdrawal operations

        Args:
            plan: Credit account Seed Plan.
            user_id: User ID.

        Returns:
            SeedAccountResult: Result with the ID of the created account and its operation details.
        """
        response = self.accounts_gateway_client.open_credit_card_account(user_id=user_id)
        card_id = response.account.cards[0].id
        account_id = response.account.id

        return SeedAccountResult(
            account_id=response.account.id,
            physical_cards=[
                self.build_physical_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.physical_cards.count)
            ],
            virtual_cards=[
                self.build_virtual_card_result(user_id=user_id, account_id=response.account.id)
                for _ in range(plan.virtual_cards.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ],
            transfer_operations=[
                self.build_transfer_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ],
            cash_withdrawal_operations=[
                self.build_cash_withdrawal_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ],
        )

    def build_user(self, plan: SeedUsersPlan) -> SeedUserResult:
        """
        Create user and does the following according to the passed Plan:
        - opens savings and deposit accounts.
        - creates debit and credit accounts with cards and operations.

        Args:
            plan: Seed User plan

        Returns:
            SeedUserResult: Result with user ID and all the created entities.
        """
        response = self.users_gateway_client.create_user()

        return SeedUserResult(
            user_id=response.user.id,
            savings_accounts=[
                self.build_savings_account_result(user_id=response.user.id)
                for _ in range(plan.savings_accounts.count)
            ],
            deposit_accounts=[
                self.build_deposit_account_result(user_id=response.user.id)
                for _ in range(plan.deposit_accounts.count)
            ],
            debit_card_accounts=[
                self.build_debit_card_account_result(plan=plan.debit_card_accounts, user_id=response.user.id)
                for _ in range(plan.debit_card_accounts.count)
            ],
            credit_card_accounts=[
                self.build_credit_card_account_result(plan=plan.credit_card_accounts, user_id=response.user.id)
                for _ in range(plan.credit_card_accounts.count)
            ]
        )

    def build(self, plan: SeedsPlan) -> SeedsResult:
        """
        Generates a final full test data structure based on the passed Plan:
        - creates a desired amount of users.
        - each user get theirs accounts, cards and operations.

        Args:
            plan: Global test data generation plan.

        Returns:
            SeedsResult: Result with all the generated users' data.
        """
        return SeedsResult(users=[self.build_user(plan=plan.users) for _ in range(plan.users.count)])


def build_grpc_seeds_builder() -> SeedsBuilder:
    """
    Seeder-generating factory with gRPC client.

    Returns:
        SeedsBuilder: Initialized seeder with gRPC-clients.
    """
    return SeedsBuilder(
        users_gateway_client=build_users_gateway_grpc_client(),
        cards_gateway_client=build_cards_gateway_grpc_client(),
        accounts_gateway_client=build_accounts_gateway_grpc_client(),
        operations_gateway_client=build_operations_gateway_grpc_client()
    )


def build_http_seeds_builder():
    """
    Seeder-generating factory with HTTP client.

    Returns:
        SeedsBuilder: Initialized seeder with HTTP-clients.
    """
    return SeedsBuilder(
        users_gateway_client=build_users_gateway_http_client(),
        cards_gateway_client=build_cards_gateway_http_client(),
        accounts_gateway_client=build_accounts_gateway_http_client(),
        operations_gateway_client=build_operations_gateway_http_client()
    )
