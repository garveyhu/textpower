from pathlib import Path

from dotenv import dotenv_values
from pydantic_settings import BaseSettings


class SystemSettings(BaseSettings):
    REDIS_HOST: str = None
    REDIS_PORT: str = None
    REDIS_DB: int = None
    REDIS_PASSWORD: str = None
    SOCKET_TIMEOUT: float = None
    REDIS_SENTINEL_MASTER: str = None
    REDIS_SENTINEL_PASSWORD: str = None

    ELASTICSEARCH_URL: str = None
    ELASTIC_USERNAME: str = None
    ELASTIC_PASSWORD: str = None

    LANGCHAIN_TRACING_V2: bool = True
    LANGCHAIN_ENDPOINT: str = None
    LANGCHAIN_API_KEY: str = None
    LANGCHAIN_PROJECT: str = None


def refresh_settings():
    env_values = dotenv_values(env_file)
    for key, value in env_values.items():
        setattr(system_settings, key, value)


config_json = Path(__file__).parent.parent.parent.parent / "config.json"
env_file = Path(__file__).parent.parent.parent.parent / ".env"
system_settings = SystemSettings(_env_file=env_file, _env_file_encoding="utf-8")