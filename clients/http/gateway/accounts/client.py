from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient


class GetAccountsQueryDict(TypedDict):
    """
    Data structure to get user accounts list.
    """
    userId: str

class OpenDepositAccountRequestDict(TypedDict):
    """
    Data structure to open a deposit account.
    """
    userId: str


class OpenSavingsAccountRequestDict(TypedDict):
    """
    Data structure to open a savings account.
    """
    userId: str


class OpenDebitCardAccountRequestDict(TypedDict):
    """
    Data structure to open a debit account.
    """
    userId: str


class OpenCreditCardAccountRequestDict(TypedDict):
    """
    Data structure to open a credit account.
    """
    userId: str

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
