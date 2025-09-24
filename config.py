from pydantic_settings import BaseSettings, SettingsConfigDict

# Import nested models
from tools.config.grpc import GRPCClientConfig
from tools.config.http import HTTPClientConfig
from tools.config.locust import LocustUserConfig


class Settings(BaseSettings):
    # Loading config — where to get vars from
    model_config = SettingsConfigDict(
        extra='allow',  # Allow extra fields (for instance, unused variables)
        env_file='.env',  # The name of the main .env file
        env_file_encoding='utf-8',
        env_nested_delimiter="."  # Allows to use nested variables, for instance: LOCUST_USER.WAIT_TIME_MIN
    )

    # Nested settings sections
    locust_user: LocustUserConfig
    gateway_http_client: HTTPClientConfig
    gateway_grpc_client: GRPCClientConfig


# Global Settings object
settings = Settings()
