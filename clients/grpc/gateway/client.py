from grpc import Channel, insecure_channel


def build_gateway_grpc_client() -> Channel:
    """
    Factory function(builder) to create a gRPC-channel to the grpc-gateway service.

    :return: gRPC-channel (Channel) listening on localhost:9003.
    """
    # Create unsafe (non-TLS) connection with gRPC-server on localhost:9003
    return insecure_channel('localhost:9003')

