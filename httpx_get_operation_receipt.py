import time

import httpx


# Create new user
create_user_payload = {
    'email': f'user.{time.time()}@example.com',
    'lastName': 'string',
    'firstName': 'string',
    'middleName': 'string',
    'phoneNumber': 'string'
}
create_user_response = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()

# Create new credit account for the user
user_id = create_user_response_data['user']['id']
credit_account_payload = {'userId': user_id}
open_credit_account_response = httpx.post(
    'http://localhost:8003/api/v1/accounts/open-credit-card-account',
    json=credit_account_payload
)
open_credit_account_response_data = open_credit_account_response.json()

# Register user purchase made with a credit card
account_id = open_credit_account_response_data['account']['id']
card_id = open_credit_account_response_data['account']['cards'][0]['id']
purchase_operation_payload = {
  'status': 'IN_PROGRESS',
  'amount': 77.99,
  'cardId': card_id,
  'accountId': account_id,
  'category': 'taxi'
}
making_purchase_response = httpx.post(
    'http://localhost:8003/api/v1/operations/make-purchase-operation',
    json=purchase_operation_payload
)
making_purchase_response_data = making_purchase_response.json()

# Get purchase operation receipt
operation_id = making_purchase_response_data['operation']['id']
getting_purchase_receipt_response = httpx.get(f'http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}')
getting_purchase_receipt_response_data = getting_purchase_receipt_response.json()

print(f'Receipt data: {getting_purchase_receipt_response_data}')
