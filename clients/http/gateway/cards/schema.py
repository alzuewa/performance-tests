from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict


class CardType(StrEnum):
    VIRTUAL = 'VIRTUAL'
    PHYSICAL = 'PHYSICAL'


class CardStatus(StrEnum):
    ACTIVE = 'ACTIVE'
    FROZEN = 'FROZEN'
    CLOSED = 'CLOSED'
    BLOCKED = 'BLOCKED'


class CardPaymentSystem(StrEnum):
    VISA = 'VISA'
    MASTERCARD = 'MASTERCARD'


class CardSchema(BaseModel):
    """
    Card data structure.
    """
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias='accountId')
    card_number: str = Field(alias='cardNumber')
    card_holder: str = Field(alias='cardHolder')
    expiry_date: date = Field(alias='expiryDate')
    payment_system: CardPaymentSystem = Field(alias='paymentSystem')


class IssueVirtualCardRequestSchema(BaseModel):
    """
    Data structure to issue a new virtual card.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')
    account_id: str = Field(alias='accountId')


class IssueVirtualCardResponseSchema(BaseModel):
    """
    Issue a new virtual card response structure.
    """
    card: CardSchema


class IssuePhysicalCardRequestSchema(BaseModel):
    """
    СData structure to issue a new physical card.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')
    account_id: str = Field(alias='accountId')


class IssuePhysicalCardResponseSchema(BaseModel):
    """
    Issue a new physical card response structure.
    """
    card: CardSchema
