from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    redis_nodes: List[str] = []
    debug: bool = False

    class Config:
        env_prefix = ""
        case_sensitive = False


settings = Settings()
