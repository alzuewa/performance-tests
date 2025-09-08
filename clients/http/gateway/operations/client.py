from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    """
    Data structure to get account operations.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Data structure to create account operations.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Data structure to create account purchase operations.
    """
    category: str


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
        Creates a fee operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-fee-operation', json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Creates a top-up operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Creates a cashback operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Creates a transfer operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Creates a purchase operation.
        :param request: Dict with operation data and purchase category.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Creates a bill-payment operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Creates a cash-withdrawal operation.
        :param request: Dict with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-cash-withdrawal-operation', json=request)


def build_documents_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Creates OperationsGatewayHTTPClient instance.
    :return: ready-to-use OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client = build_gateway_http_client())
