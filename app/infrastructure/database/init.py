from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from settings.config import config


DB_USER: str = config.DB_USER
DB_PASSWORD: str = config.DB_PASSWORD
DB_ADDRESS: str = config.DB_ADDRESS
DB_NAME: str = config.DB_NAME

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}",
)


class Base(DeclarativeBase):
    pass
