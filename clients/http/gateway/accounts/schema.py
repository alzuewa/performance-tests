from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict

from clients.http.gateway.cards.schema import CardSchema


class AccountType(StrEnum):
    DEPOSIT = 'DEPOSIT'
    SAVINGS = 'SAVINGS'
    DEBIT_CARD = 'DEBIT_CARD'
    CREDIT_CARD = 'CREDIT_CARD'


class AccountStatus(StrEnum):
    ACTIVE = 'ACTIVE'
    CLOSED = 'CLOSED'
    PENDING_CLOSURE = 'PENDING_CLOSURE'


class AccountSchema(BaseModel):
    """
    Account data structure.
    """
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(BaseModel):
    """
    Data structure to get user accounts list.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class GetAccountsResponseSchema(BaseModel):
    """
    Get accounts list response data structure.
    """
    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(BaseModel):
    """
    Data structure to open a deposit account.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class OpenDepositAccountResponseSchema(BaseModel):
    """
    Open deposit account response data structure.
    """
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """
    Data structure to open a savings account.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class OpenSavingsAccountResponseSchema(BaseModel):
    """
    Open savings account response data structure.
    """
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """
    Data structure to open a debit account.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class OpenDebitCardAccountResponseSchema(BaseModel):
    """
    Open debit account response data structure.
    """
    account: AccountSchema


class OpenCreditCardAccountRequestSchema(BaseModel):
    """
    Data structure to open a credit account.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class OpenCreditCardAccountResponseSchema(BaseModel):
    """
    Open credit account response data structure.
    """
    account: AccountSchema
