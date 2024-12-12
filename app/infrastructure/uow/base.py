from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from infrastructure.repository.base import BaseBatchRepository
from pytest import Session


@dataclass
class BaseUnitOfWork(ABC):
    batches_repository: BaseBatchRepository
    session: Session

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self): ...

    @abstractmethod
    def rollback(self): ...
