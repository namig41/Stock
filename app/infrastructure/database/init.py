from infrastructure.exceptions.repository import BatchNotFoundInDataException
from infrastructure.logger.base import ILogger
from sqlalchemy import (
    create_engine,
    Engine,
)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase

from settings.config import config


DB_USER: str = config.DB_USER
DB_PASSWORD: str = config.DB_PASSWORD
DB_ADDRESS: str = config.DB_ADDRESS
DB_NAME: str = config.DB_NAME


def init_database(logger: ILogger) -> Engine:
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}",
    )

    try:
        with engine.connect():
            logger.info("Успешное подключение к базе данных")
    except SQLAlchemyError:
        logger.error("Ошибка подключения к базе данных")
        raise BatchNotFoundInDataException()
    return engine


class Base(DeclarativeBase):
    pass
