import time

import httpx

create_user_payload = {
    'email': f'user.{time.time()}@example.com',
    'lastName': 'string',
    'firstName': 'string',
    'middleName': 'string',
    'phoneNumber': 'string'
}

create_user_response = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()

user_id = create_user_response_data['user']['id']
deposit_account_payload = {'userId': user_id}

open_deposit_account_response = httpx.post(
    'http://localhost:8003/api/v1/accounts/open-deposit-account',
    json=deposit_account_payload
)

print('Open deposit account response:', open_deposit_account_response.json())
print('Status code:', open_deposit_account_response.status_code)
