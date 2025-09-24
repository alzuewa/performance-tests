from pydantic import BaseModel, HttpUrl


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float = 100.0

    @property
    def client_url(self) -> str:
        """
        Returns string representation of the URL suitable for passing to httpx.Client.
        httpx.Client requires base_url as a string.
        """
        return str(self.url)

