from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from domain.entities.batch import Batch


@dataclass
class BaseBatchRepository(ABC):
    @abstractmethod
    def add_batch(self, batch: Batch): ...

    @abstractmethod
    def get_batches(self) -> Iterable[Batch]: ...

    @abstractmethod
    def get_batch(self, reference: str) -> Batch | None: ...
