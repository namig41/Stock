from functools import lru_cache

from infrastructure.repository.base import BaseRepository
from infrastructure.repository.sqlite import SQLiteBatchRepository


@lru_cache(1)
def init_repository() -> BaseRepository:
    repository: BaseRepository = SQLiteBatchRepository("app/infrastructure/db/db")
    return repository
