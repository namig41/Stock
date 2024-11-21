from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PYTHONPATH: str
    API_PORT: int

    DB_USER: str
    DB_PASSWORD: str
    DB_ADDRESS: str
    DB_NAME: str


config = Settings()
