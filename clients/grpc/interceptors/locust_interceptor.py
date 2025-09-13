import time

from grpc import UnaryUnaryClientInterceptor, RpcError
from locust.env import Environment


class LocustInterceptor(UnaryUnaryClientInterceptor):

    def __init__(self, environment: Environment):
        self.environment = environment

    def intercept_unary_unary(self, continuation, client_call_details, request):
        response = None
        exception: RpcError | None = None
        start_time = time.perf_counter()
        response_length = 0

        try:
            response = continuation(client_call_details, request)
            response_length = response.result().ByteSize()
        except RpcError as error:
            exception = error

        response_time = (time.perf_counter() - start_time) * 1000

        self.environment.events.request.fire(
            name=client_call_details.method,
            request_type='gRPC',
            context=None,
            response_time=response_time,
            response=response,
            exception=exception,
            response_length=response_length,
         )

        return response
