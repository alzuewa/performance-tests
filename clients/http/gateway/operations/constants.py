from enum import StrEnum


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
