from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_VERSION: int = 1
    ALLOWED_ORIGINS: List[str] = [
        '*'
    ]

    class Config:
        case_sensitive = True


settings = Settings()
