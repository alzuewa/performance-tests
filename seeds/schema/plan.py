from pydantic import BaseModel, Field


class SeedCardsPlan(BaseModel):
    """
    Generating account cards plan.

    Attributes:
        count (int): Number of cards to generate (virtual/physical).
    """
    count: int = 0


class SeedOperationsPlan(BaseModel):
    """
    Generating account operations plan.

    Attributes:
        count (int): Number of operations to generate (fulfills/withdrawals).
    """
    count: int = 0


class SeedAccountsPlan(BaseModel):
    """
    A plan for generating accounts of different types (i.e. deposit, credit).

    Attributes:
        count (int): Number of accounts of a dedicated type.
        physical_cards (SeedCardsPlan): A plan to create physical cards for the account.
        top_up_operations (SeedOperationsPlan): A plan to create withdrawal operations.
        purchase_operations (SeedOperationsPlan): A plan to create purchase operations.
    """
    count: int = 0
    physical_cards: SeedCardsPlan = Field(default_factory=SeedCardsPlan)
    top_up_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)
    purchase_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)


class SeedUsersPlan(BaseModel):
    """
    A plan to generate users and their accounts of different types.

    Attributes:
        count (int): Users amount.
        deposit_accounts (SeedAccountsPlan): A plan for deposit accounts.
        savings_accounts (SeedAccountsPlan): A plan for savings accounts.
        debit_card_accounts (SeedAccountsPlan): A plan for debit cards accounts.
        credit_card_accounts (SeedAccountsPlan): A plan for credit cards accounts.
    """
    count: int = 0
    deposit_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    savings_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    debit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    credit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)


class SeedsPlan(BaseModel):
    """
    The main seeding model.

    Attributes:
        users (SeedUsersPlan): A plan to create users with all the data.
    """
    users: SeedUsersPlan = Field(default_factory=SeedUsersPlan)


# Usage example:
# plan = SeedsPlan(
#     users=SeedUsersPlan(
#         count=1000,
#         debit_card_accounts=SeedAccountsPlan(
#             count=3,
#             physical_cards=SeedCardsPlan(count=3),
#             top_up_operations=SeedOperationsPlan(count=10)
#         )
#     )
# )
#
# print(plan.model_dump_json(indent=2, exclude_defaults=True))