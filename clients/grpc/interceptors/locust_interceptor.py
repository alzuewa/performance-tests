import time

from grpc import UnaryUnaryClientInterceptor, RpcError
from locust.env import Environment


class LocustInterceptor(UnaryUnaryClientInterceptor):
    """
    gRPC-interceptor to collect metrics for Locust.
    Used to measure request-response time and register request success/errors.
    """

    def __init__(self, environment: Environment):
        """
        :param environment: Locust environment object instance which holds events with metrics collection.
        """
        self.environment = environment

    def intercept_unary_unary(self, continuation, client_call_details, request):
        """
        Method to intercept unary-unary gRPC calls.

        :param continuation: Function which calls gRPC method itself.
        :param client_call_details: Request details (method, metadata, timeout, etc.).
        :param request: Request object sent to the server.
        :return: gRPC response (future-object).
        """
        response = None
        exception: RpcError | None = None
        start_time = time.perf_counter()
        response_length = 0

        try:
            # Make gRPC method call and get response-future
            response = continuation(client_call_details, request)

            # Get response length if response is already available (for metrics)
            response_length = response.result().ByteSize()
        except RpcError as error:
            exception = error

        # Evaluate response time in ms
        response_time = (time.perf_counter() - start_time) * 1000

        # Register request in Locust metrics system
        self.environment.events.request.fire(
            name=client_call_details.method,  # Method name (i.e. '/users.UsersService/CreateUser')
            request_type='gRPC',
            context=None,  # Used to pass custom data
            response_time=response_time,
            response=response,
            exception=exception,
            response_length=response_length,
        )

        # Return request result as a future-object
        return response
