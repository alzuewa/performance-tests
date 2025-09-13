from grpc import Channel, insecure_channel, intercept_channel
from locust.env import Environment

from clients.grpc.interceptors.locust_interceptor import LocustInterceptor


def build_gateway_grpc_client() -> Channel:
    """
    Factory function(builder) to create a gRPC-channel to the grpc-gateway service.

    :return: gRPC-channel (Channel) listening on localhost:9003.
    """
    # Create unsafe (non-TLS) connection with gRPC-server on localhost:9003
    return insecure_channel('localhost:9003')

def build_gateway_locust_grpc_client(environment: Environment) -> Channel:
    locust_interceptor = LocustInterceptor(environment)

    channel = insecure_channel('localhost:9003')
    return intercept_channel(channel, locust_interceptor)
