from enum import StrEnum

from httpx import URL
from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class OperationType(StrEnum):
    FEE = 'FEE'
    TOP_UP = 'TOP_UP'
    PURCHASE = 'PURCHASE'
    CASHBACK = 'CASHBACK'
    TRANSFER = 'TRANSFER'
    BILL_PAYMENT = 'BILL_PAYMENT'
    CASH_WITHDRAWAL = 'CASH_WITHDRAWAL'


class OperationStatus(StrEnum):
    FAILED = 'FAILED'
    COMPLETED = 'COMPLETED'
    IN_PROGRESS = 'IN_PROGRESS'
    UNSPECIFIED = 'UNSPECIFIED'
    
    
class OperationSchema(BaseModel):
    """
    Operation data structure.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias='cardId')
    category: str
    created_at: str = Field(alias='createdAt')
    account_id: str = Field(alias='accountId')


class GetOperationResponseSchema(BaseModel):
    """
    Get operation response data structure.
    """
    operation: OperationSchema


class MakeOperationResponseSchema(BaseModel):
    """
    Make operation response data structure.
    """
    operation: OperationSchema


class OperationReceiptSchema(BaseModel):
    """
    Operation receipt data structure.
    """
    url: HttpUrl | str
    document: str


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Get operation receipt response data structure.
    """
    receipt: OperationReceiptSchema


class OperationsSummarySchema(BaseModel):
    """
    Operations summary data structure.
    """
    spent_amount: float = Field(alias='spentAmount')
    received_amount: float = Field(alias='receivedAmount')
    cashback_amount: float = Field(alias='cashbackAmount')


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Get operations summary response data structure.
    """
    summary: OperationsSummarySchema


class GetOperationsQuerySchema(BaseModel):
    """
    Data structure to get account operations.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias='accountId')


class GetOperationsResponseSchema(BaseModel):
    """
    Get operations list response data structure.
    """
    operations: list[OperationSchema]


class MakeOperationRequestSchema(BaseModel):
    """
    Data structure to make account operations.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias='cardId')
    account_id: str = Field(alias='accountId')


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure to make account purchase operations.
    """
    category: str


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure to make account fee operations.
    """

class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure to make account top up operations.
    """

class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure to make account bill payment operations.
    """


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure to make account cash withdrawal operations.
    """

class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure to make account cashback operations.
    """


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Data structure to make account transfer operations.
    """