from functools import lru_cache

from infrastructure.database.init import init_database
from infrastructure.logger.base import ILogger
from infrastructure.logger.logger import create_logger_dependency
from infrastructure.repository.base import BaseBatchRepository
from infrastructure.repository.memory import MemoryBatchRepository
from punq import (
    Container,
    Scope,
)
from sqlalchemy import Engine


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container: Container = Container()

    container.register(
        ILogger,
        factory=create_logger_dependency,
        scope=Scope.singleton,
    )

    container.register(
        BaseBatchRepository,
        MemoryBatchRepository,
        scope=Scope.singleton,
    )

    container.register(
        Engine,
        factory=init_database,
        scope=Scope.singleton,
    )

    return container
