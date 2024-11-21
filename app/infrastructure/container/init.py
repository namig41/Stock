from functools import lru_cache

from infrastructure.repository.base import BaseBatchRepository
from infrastructure.repository.memory import MemoryBatchRepository
from punq import (
    Container,
    Scope,
)


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container: Container = Container()
    container.register(
        BaseBatchRepository,
        MemoryBatchRepository,
        scope=Scope.singleton,
    )
    return container
