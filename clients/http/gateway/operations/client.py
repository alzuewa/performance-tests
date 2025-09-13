from httpx import QueryParams, Response
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema, 
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashbackOperationRequestSchema,
    MakeFeeOperationRequestSchema,
    MakeOperationRequestSchema,
    MakeOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakeTopUpOperationRequestSchema,
    MakeTransferOperationRequestSchema,
)


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
        return self.get(
            f'/api/v1/operations/{operation_id}',
            extensions=HTTPClientExtensions(route='/api/v1/operations/{operation_id}')
        )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Gets user account operation receipt by operation_id.
        :param operation_id: id of the operation.
        :return: Response object with response data.
        """
        return self.get(
            f'/api/v1/operations/operation-receipt/{operation_id}',
            extensions=HTTPClientExtensions(route='/api/v1/operations/operation-receipt/{operation_id}')
        )

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Gets user account operations list.
        :param query: Pydantic-model with request params.
        :return: Response object with response data.
        """
        return self.get(
            '/api/v1/operations',
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route='/api/v1/operations')
        )

    def get_operations_summary_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Gets user account operations summary.
        :param query: Pydantic-model with request params.
        :return: Response object with response data.
        """
        return self.get(
            '/api/v1/operations/operations-summary',
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route='/api/v1/operations/operations-summary')
        )

    def make_fee_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Makes a fee operation.
        :param request: Pydantic-model with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-fee-operation', json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Makes a top-up operation.
        :param request: Pydantic-model with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Makes a cashback operation.
        :param request: Pydantic-model with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Makes a transfer operation.
        :param request: Pydantic-model with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Makes a purchase operation.
        :param request: Pydantic-model with operation data and purchase category.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Makes a bill-payment operation.
        :param request: Pydantic-model with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Makes a cash-withdrawal operation.
        :param request: Pydantic-model with operation data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/operations/make-cash-withdrawal-operation', json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query=query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query=query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_fee_operation_api(request)
        return MakeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_top_up_operation_api(request)
        return MakeOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cashback_operation_api(request)
        return MakeOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_transfer_operation_api(request)
        return MakeOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakeOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_purchase_operation_api(request)
        return MakeOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_bill_payment_operation_api(request)
        return MakeOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Creates OperationsGatewayHTTPClient instance.
    :return: ready-to-use OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client = build_gateway_http_client())

def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Creates OperationsGatewayHTTPClient adapted for Locust.

    Client automatically collects metrics and passes it to Locust by the means of hooks.
    Is used exceptionally for load testing.

    :param environment: Locust environment object.
    :return: ready-to-use OperationsGatewayHTTPClient with hooks to collect metrics.
    """
    return OperationsGatewayHTTPClient(client = build_gateway_locust_http_client(environment))
