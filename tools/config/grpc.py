from pydantic import BaseModel


class GRPCClientConfig(BaseModel):
    port: int

    # i.e. localhost or grpc-gateway.internal
    host: str

    @property
    def client_url(self) -> str:
        """
        Returns connection point as host:port required to create a gRPC-channel with insecure_channel().
        """
        return f'{self.host}:{self.port}'
