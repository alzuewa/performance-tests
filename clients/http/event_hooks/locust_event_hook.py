import time

from httpx import HTTPError, HTTPStatusError, Request, Response
from locust.env import Environment

def locust_request_event_hook(request: Request) -> None:
    """
    httpx event hook; is invoked before sending a request.

    Stores current timestamp in `request.extensions['start_time']`
    to evaluate response time further.
    """
    request.extensions['start_time'] = time.perf_counter()

def locust_response_event_hook(environment: Environment):
    """
    Returns a httpx event hook which is invoked after getting a response.

    Uses `request.extensions['start_time']` to evaluate response time.
    Extracts route from `request.extensions['route']` if was passed.
    Sends gathered metrics to `environment.events.request` so that Locust can aggregate statistics.

    :param environment: Locust environment object through which the metrics are sent.
    :return: Hook function for httpx response event hook.
    """
    def inner(response: Response) -> None:
        exception = None
        try:
            response = response.raise_for_status()
        except (HTTPError, HTTPStatusError) as error:
            exception = error

        request = response.request
        route = request.extensions.get('route', request.url.path)
        start_time = request.extensions.get('start_time')
        response_time = (time.perf_counter() - start_time) * 1000
        response_length = len(response.read())

        environment.events.request.fire(
            name=f'{request.method} {route}',
            response_time=response_time,
            context=None,
            response=response,
            exception=exception,
            request_type='HTTP',
            response_length =response_length,
        )
    return inner