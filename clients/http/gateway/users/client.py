from httpx import Response
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema


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
        return self.get(
            f'/api/v1/users/{user_id}',
            extensions=HTTPClientExtensions(route='/api/v1/users/{user_id}')
        )

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Creates a new user.

        :param request: Pydantic-model with a new user data.
        :return: Response object with response data.
        """
        return self.post('/api/v1/users', json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        request = CreateUserRequestSchema()
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Creates UsersGatewayHTTPClient instance.
    :return: ready-to-use UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())


def build_users_gateway_locust_http_client(environment: Environment) -> UsersGatewayHTTPClient:
    """
    Creates UsersGatewayHTTPClient adapted for Locust.

    Client automatically collects metrics and passes it to Locust by the means of hooks.
    Is used exceptionally for load testing.

    :param environment: Locust environment object.
    :return: ready-to-use UsersGatewayHTTPClient with hooks to collect metrics.
    """
    return UsersGatewayHTTPClient(client=build_gateway_locust_http_client(environment))
