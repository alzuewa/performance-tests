from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.cards.client import CardDict
from clients.http.gateway.client import build_gateway_http_client


class AccountDict(TypedDict):
    """
    Account data structure.
    """
    id: str
    type: str
    cards: list[CardDict]
    status: str
    balance: float


class GetAccountsQueryDict(TypedDict):
    """
    Data structure to get user accounts list.
    """
    userId: str


class GetAccountsResponseDict(TypedDict):
    """
    Get accounts list response data structure.
    """
    accounts: list[AccountDict]


class OpenDepositAccountRequestDict(TypedDict):
    """
    Data structure to open a deposit account.
    """
    userId: str


class OpenDepositAccountResponseDict(TypedDict):
    """
    Open deposit account response data structure.
    """
    account: AccountDict


class OpenSavingsAccountRequestDict(TypedDict):
    """
    Data structure to open a savings account.
    """
    userId: str


class OpenSavingsAccountResponseDict(TypedDict):
    """
    Open savings account response data structure.
    """
    account: AccountDict


class OpenDebitCardAccountRequestDict(TypedDict):
    """
    Data structure to open a debit account.
    """
    userId: str


class OpenDebitCardAccountResponseDict(TypedDict):
    """
    Open debit account response data structure.
    """
    account: AccountDict


class OpenCreditCardAccountRequestDict(TypedDict):
    """
    Data structure to open a credit account.
    """
    userId: str


class OpenCreditCardAccountResponseDict(TypedDict):
    """
    Open credit account response data structure.
    """
    account: AccountDict

class AccountsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with http-gateway /api/v1/accounts service.
    """

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """
        Gets user accounts list.
        :param query: Dict with request params.
        :return: Response object with response data.
        """
        return self.get('/api/v1/accounts', params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        """
        Opens a deposit account.
        :param request: Dict with userId.
        :return: Response object with response data.
        """
        return self.post('/api/v1/accounts/open-deposit-account', json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        """
        Opens a savings account.
        :param request: Dict with userId.
        :return: Response object with response data.
        """
        return self.post('/api/v1/accounts/open-savings-account', json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        """
        Opens a debit account.
        :param request: Dict with userId.
        :return: Response object with response data.
        """
        return self.post('/api/v1/accounts/open-debit-card-account', json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        """
        Opens a credit account.
        :param request: Dict with userId.
        :return: Response object with response data.
        """
        return self.post('/api/v1/accounts/open-credit-card-account', json=request)

    def get_accounts(self, user_id: str) -> GetAccountsResponseDict:
        query = GetAccountsQueryDict(userId=user_id)
        response = self.get_accounts_api(query)
        return response.json()

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseDict:
        request = OpenDepositAccountRequestDict(userId=user_id)
        response = self.open_deposit_account_api(request)
        return response.json()

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseDict:
        request = OpenSavingsAccountRequestDict(userId=user_id)
        response = self.open_savings_account_api(request)
        return response.json()

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseDict:
        request = OpenDebitCardAccountRequestDict(userId=user_id)
        response = self.open_debit_card_account_api(request)
        return response.json()

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseDict:
        request = OpenCreditCardAccountRequestDict(userId=user_id)
        response = self.open_credit_card_account_api(request)
        return response.json()


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Creates AccountsGatewayHTTPClient instance.
    :return: ready-to-use AccountsGatewayHTTPClient.
    """
    return AccountsGatewayHTTPClient(client = build_gateway_http_client())
