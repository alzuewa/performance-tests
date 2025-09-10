import grpc

from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse
)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub

from tools.fakers import fake

# Create a connection with a gRPC-server on localhost:9003
channel = grpc.insecure_channel('localhost:9003')

# Create gRPC-clients for UsersGatewayService and AccountsGatewayService
users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)

# Prepare request data to create a new user
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)

# Send request to create user and save response data
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print('Create user response: ', create_user_response)

# Prepare request data to open a debit card account for previously created user
open_debit_card_account_request = OpenDebitCardAccountRequest(user_id=create_user_response.user.id)

# Send request to open a debit card account
open_debit_card_account_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(
    open_debit_card_account_request
)
print('Open debit card account response: ', open_debit_card_account_response)
