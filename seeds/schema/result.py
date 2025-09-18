import random

from pydantic import BaseModel, Field


class SeedCardResult(BaseModel):
    """
    The result of card generation.

    Attributes:
        card_id (str): Unique ID of the card.
    """
    card_id: str


class SeedOperationResult(BaseModel):
    """
    The result of operation generation.

    Attributes:
        operation_id (str): Unique ID of the operation.
    """
    operation_id: str


class SeedAccountResult(BaseModel):
    """
    The result of generating an account with all nested entities.

    Attributes:
        account_id (str): Unique ID of the account.
        physical_cards (list[SeedCardResult]): Account physical cards list.
        virtual_cards (list[SeedCardResult]): Account virtual cards list.
        top_up_operations (list[SeedOperationResult]): Account top-ups list.
        purchase_operations (list[SeedOperationResult]): Account purchases list.
        transfer_operations (list[SeedOperationResult]): Account transfers list.
        cash_withdrawal_operations (list[SeedOperationResult]): Account cash withdrawals list.
    """
    account_id: str
    physical_cards: list[SeedCardResult] = Field(default_factory=list)
    virtual_cards: list[SeedCardResult] = Field(default_factory=list)
    top_up_operations: list[SeedOperationResult] = Field(default_factory=list)
    purchase_operations: list[SeedOperationResult] = Field(default_factory=list)
    transfer_operations: list[SeedOperationResult] = Field(default_factory=list)
    cash_withdrawal_operations: list[SeedOperationResult] = Field(default_factory=list)


class SeedUserResult(BaseModel):
    """
    The result of generating a user with their accounts.

    Attributes:
        user_id (str): Unique ID of the user.
        deposit_accounts (list[SeedAccountResult]): Deposit accounts list.
        savings_accounts (list[SeedAccountResult]): Savings accounts list.
        debit_card_accounts (list[SeedAccountResult]): Debit accounts list.
        credit_card_accounts (list[SeedAccountResult]): Credit accounts list.
    """
    user_id: str
    deposit_accounts: list[SeedAccountResult] = Field(default_factory=list)
    savings_accounts: list[SeedAccountResult] = Field(default_factory=list)
    debit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)
    credit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)


class SeedsResult(BaseModel):
    """
    The main model of seeding result — aggregates all the generated users

    Attributes:
        users (list[SeedUserResult]): СThe list of generated users.
    """

    users: list[SeedUserResult] = Field(default_factory=list)

    def get_next_user(self) -> SeedUserResult:
        """
        Returns and deletes the first user from the list.

        Used when for each Virtual User a new test user is required.

        Returns:
            SeedUserResult: The next user from the list.
        """
        return self.users.pop(0)

    def get_random_user(self) -> SeedUserResult:
        """
        Returns a random user from the list without deleting it.

        Used when the order is not important and the user is chosen randomly.

        Returns:
            SeedUserResult: A random user.
        """
        return random.choice(self.users)
