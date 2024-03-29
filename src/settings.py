from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    ECHO_DB: bool = True


@lru_cache
def get_settings():
    return Settings()
