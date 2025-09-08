from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class CreateUserRequestDict(TypedDict):
    """
    Data structure to create a new user
    """
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UsersGatewayHTTPClient(HTTPClient):
    """
    Client to interact with http-gateway /api/v1/users service.
    """

    def get_user_api(self, user_id: str) -> Response:
        """
       Gets user data by user_id.

       :param user_id: id of the user.
       :return: Response object with response data.
       """
        return self.get(f'/api/v1/users/{user_id}')

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Creates a new user.

        :param request: Dict with a new user data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/users', json=request)
