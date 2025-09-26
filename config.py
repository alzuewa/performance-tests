import locust.stats  # Locust module responsible for gathering and storing statistics
from pydantic_settings import BaseSettings, SettingsConfigDict

# Import nested models
from tools.config.grpc import GRPCClientConfig
from tools.config.http import HTTPClientConfig
from tools.config.locust import LocustUserConfig

# Which percentiles will be shown in Locust reports
locust.stats.PERCENTILES_TO_REPORT = [0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99, 1.0]

locust.stats.CSV_STATS_INTERVAL_SEC = 5

locust.stats.HISTORY_STATS_INTERVAL_SEC = 5

locust.stats.CONSOLE_STATS_INTERVAL_SEC = 5

locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 5


class Settings(BaseSettings):
    # Loading config — where to get vars from
    model_config = SettingsConfigDict(
        extra='allow',  # Allow extra fields (for instance, unused variables)
        env_file='.env',  # The name of the main .env file
        env_file_encoding='utf-8',
        env_nested_delimiter='.'  # Allows to use nested variables, for instance: LOCUST_USER.WAIT_TIME_MIN
    )

    # Nested settings sections
    locust_user: LocustUserConfig
    gateway_http_client: HTTPClientConfig
    gateway_grpc_client: GRPCClientConfig


# Global Settings object
settings = Settings()
