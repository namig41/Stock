from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from infrastructure.repository.base import BaseBatchRepository


@dataclass
class BaseUnitOfWork(ABC):
    batches_repository: BaseBatchRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self): ...

    @abstractmethod
    def rollback(self): ...
