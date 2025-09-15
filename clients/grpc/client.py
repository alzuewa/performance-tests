import grpc.experimental.gevent as grpc_gevent
from grpc import Channel

grpc_gevent.init_gevent()


class GRPCClient:
    """
    Base class for gRPC-client.

    It provides a common Channel to connect to a gRPC-server.
    It is a parent class for other specific clients.
    """

    def __init__(self, channel: Channel):
        """
        Base class constructor.

        :param channel: gRPC-channel to connect to the server.
                        Is created once to reuse further.
        """
        self.channel = channel
