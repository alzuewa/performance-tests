from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
documents_gateway_client = build_documents_gateway_http_client()

# Create user
create_user_response = users_gateway_client.create_user()
print(f'Create user response: {create_user_response}')

# Open credit account
open_debit_card_account_response = accounts_gateway_client.open_credit_card_account(
    user_id=create_user_response.user.id
)
print(f'Open credit card account response: {open_debit_card_account_response}')

# Get tariff document
get_tariff_docs_response = documents_gateway_client.get_tariff_document(
    account_id=open_debit_card_account_response['account']['id']
)
print(f'Get tariff document response: {get_tariff_docs_response}')

# Get contract document
get_contract_docs_response = documents_gateway_client.get_contract_document(
    account_id=open_debit_card_account_response['account']['id']
)
print(f'Get contract document response: {get_contract_docs_response}')
