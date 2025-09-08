from httpx import Client


def build_gateway_http_client() -> Client:
    """
    Creates httpx.Client instance with basic setup for http-gateway service.
    :return: ready-to-use httpx.Client object instance.
    """
    return Client(base_url='http://localhost:8003', timeout=100)
