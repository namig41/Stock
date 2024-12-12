from functools import lru_cache

from infrastructure.database.init import init_database
from infrastructure.logger.base import BaseLogger
from infrastructure.logger.logger import create_logger_dependency
from infrastructure.repository.base import BaseBatchRepository
from infrastructure.repository.postgres import PostgreSQLBatchRepository
from punq import (
    Container,
    Scope,
)
from sqlalchemy import Engine


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    # Регистрируем логгер
    container.register(
        BaseLogger,
        factory=create_logger_dependency,
        scope=Scope.singleton,
    )

    # Регистрируем движок БД
    container.register(
        Engine,
        factory=init_database,
        scope=Scope.singleton,
    )

    # Регистрируем репозиторий
    container.register(
        BaseBatchRepository,
        PostgreSQLBatchRepository,
        scope=Scope.singleton,
    )

    return container
