from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()

create_user_response_data = users_gateway_client.create_user()
print('Create user data:', create_user_response_data)

get_user_response_data = users_gateway_client.get_user(create_user_response_data.user.id)
print('Get user data:', get_user_response_data)
