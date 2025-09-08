from typing import TypedDict

from httpx import QueryParams, Response, URL

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.constants import OperationStatus, OperationType


class OperationDict(TypedDict):
    """
    Operation data structure.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationResponseDict(TypedDict):
    """
    Get operation response data structure.
    """
    operation: OperationDict


class MakeOperationResponseDict(TypedDict):
    """
    Make operation response data structure.
    """
    operation: OperationDict


class OperationReceiptDict(TypedDict):
    """
    Operation receipt data structure.
    """
    url: URL | str
    document: str


class GetOperationReceiptResponseDict(TypedDict):
    """
    Get operation receipt response data structure.
    """
    receipt: OperationReceiptDict


class OperationsSummaryDict(TypedDict):
    """
    Operations summary data structure.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Get operations summary response data structure.
    """
    summary: OperationsSummaryDict


class GetOperationsQueryDict(TypedDict):
    """
    Data structure to get account operations.
    """
    accountId: str


class GetOperationsResponseDict(TypedDict):
    """
    Get operations list response data structure.
    """
    operations: list[OperationDict]


class MakeOperationRequestDict(TypedDict):
    """
    Data structure to make account operations.
    """
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure to make account purchase operations.
    """
    category: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure to make account fee operations.
    """

class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure to make account top up operations.
    """

class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure to make account bill payment operations.
    """


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure to make account cash withdrawal operations.
    """

class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure to make account cashback operations.
    """


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure to make account transfer operations.
    """


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with http-gateway /api/v1/operations service.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Gets user account operation by operation_id.
        :param operation_id: id of the operation.
        :return: Response object with response data.
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Gets user account operation receipt by operation_id.
        :param operation_id: id of the operation.
        :return: Response object with response data.
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Gets user account operations list.
        :param query: Dict with request params.
        :return: Response object with response data.
        """
        return self.get('/api/v1/operations', params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Gets user account operations summary.
        :param query: Dict with request params.
        :return: Response object with response data.
        """
        return self.get('/api/v1/operations/operations-summary', params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Makes a fee operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-fee-operation', json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Makes a top-up operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Makes a cashback operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Makes a transfer operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Makes a purchase operation.
        :param request: Dict with operation data and purchase category.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Makes a bill-payment operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Makes a cash-withdrawal operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-cash-withdrawal-operation', json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query=query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category='food'
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Creates OperationsGatewayHTTPClient instance.
    :return: ready-to-use OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client = build_gateway_http_client())
