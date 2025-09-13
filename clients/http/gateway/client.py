import logging
from httpx import Client
from locust.env import Environment

from clients.http.event_hooks.locust_event_hook import locust_request_event_hook, locust_response_event_hook


def build_gateway_http_client() -> Client:
    """
    Creates httpx.Client instance with basic setup for http-gateway service.
    :return: ready-to-use httpx.Client object instance.
    """
    return Client(base_url='http://localhost:8003', timeout=100)

def build_gateway_locust_http_client(environment: Environment) -> Client:
    """
    HTTP-client specifically designed for load testing with Locust.

    Specifics:
    - adds `locust_request_event_hook` to get and store a request start time,
    - adds `locust_response_event_hook` evaluating metrics
    (response time, response length, etc.) and sends it to Locust in `environment.events.request.fire()`.

    Hence, this client automatically reports statistics to Locust with every HTTP-request.

    :param environment: Locust environment object through which the metrics are sent.
    :return: httpx.Client with hooks plugged in specifically for load testing.
    """
    logging.getLogger('httpx').setLevel(logging.WARNING)

    return Client(
        base_url='http://localhost:8003',
        timeout=100,
        event_hooks={
            'request': [locust_request_event_hook],
            'response': [locust_response_event_hook(environment)]
        }
    )
