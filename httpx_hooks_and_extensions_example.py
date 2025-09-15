from datetime import datetime

from httpx import Client, Request, Response


def log_request_hook(request: Request):
    request.extensions['start_time'] = datetime.now()
    print(f'REQUEST: {request.method}')


def log_response_hook(response: Response):
    duration = datetime.now() - response.request.extensions['start_time']
    print(f'RESPONSE: {response.status_code}, {duration}')


client = Client(
    base_url='http://localhost:8003',
    event_hooks={'request': [log_request_hook], 'response': [log_response_hook]}
)
resp = client.get('/api/v1/users/9259ff0e-a3f6-45a7-97e6-50e20ef77bed')

print(resp)
print(resp.request.extensions)
