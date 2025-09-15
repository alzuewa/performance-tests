from httpx import QueryParams, Response
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.accounts.schema import (
    GetAccountsQuerySchema,
    GetAccountsResponseSchema,
    OpenDepositAccountRequestSchema,
    OpenDepositAccountResponseSchema,
    OpenSavingsAccountRequestSchema,
    OpenSavingsAccountResponseSchema,
    OpenDebitCardAccountRequestSchema,
    OpenDebitCardAccountResponseSchema,
    OpenCreditCardAccountRequestSchema,
    OpenCreditCardAccountResponseSchema
)
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with http-gateway /api/v1/accounts service.
    """

    def get_accounts_api(self, query: GetAccountsQuerySchema) -> Response:
        """
        Gets user accounts list.
        :param query: Pydantic-model with request params.
        :return: Response object with response data.
        """
        return self.get(
            '/api/v1/accounts',
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route='/api/v1/accounts')
        )

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        """
        Opens a deposit account.
        :param request: Pydantic-model with userId.
        :return: Response object with response data.
        """
        return self.post('/api/v1/accounts/open-deposit-account', json=request.model_dump(by_alias=True))

    def open_savings_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        """
        Opens a savings account.
        :param request: Pydantic-model with userId.
        :return: Response object with response data.
        """
        return self.post('/api/v1/accounts/open-savings-account', json=request.model_dump(by_alias=True))

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        """
        Opens a debit account.
        :param request: Pydantic-model with userId.
        :return: Response object with response data.
        """
        return self.post('/api/v1/accounts/open-debit-card-account', json=request.model_dump(by_alias=True))

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        """
        Opens a credit account.
        :param request: Pydantic-model with userId.
        :return: Response object with response data.
        """
        return self.post('/api/v1/accounts/open-credit-card-account', json=request.model_dump(by_alias=True))

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        request = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseSchema:
        request = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.open_savings_account_api(request)
        return OpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseSchema:
        request = OpenDebitCardAccountRequestSchema(user_id=user_id)
        response = self.open_debit_card_account_api(request)
        return OpenDebitCardAccountResponseSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseSchema:
        request = OpenCreditCardAccountRequestSchema(user_id=user_id)
        response = self.open_credit_card_account_api(request)
        return OpenCreditCardAccountResponseSchema.model_validate_json(response.text)


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Creates AccountsGatewayHTTPClient instance.
    :return: ready-to-use AccountsGatewayHTTPClient.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())


def build_accounts_gateway_locust_http_client(environment: Environment) -> AccountsGatewayHTTPClient:
    """
    Creates AccountsGatewayHTTPClient adapted for Locust.

    Client automatically collects metrics and passes it to Locust by the means of hooks.
    Is used exceptionally for load testing.

    :param environment: Locust environment object.
    :return: ready-to-use AccountsGatewayHTTPClient with hooks to collect metrics.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))
