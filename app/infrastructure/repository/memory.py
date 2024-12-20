from dataclasses import (
    dataclass,
    field,
)
from typing import Iterable

from infrastructure.exceptions.repository import BatchNotFoundInDataException
from infrastructure.repository.base import BaseBatchRepository

from domain.entities.batch import Batch


@dataclass
class MemoryBatchRepository(BaseBatchRepository):
    _saved_batches: set[Batch] = field(
        default_factory=set,
    )

    def add_batch(self, batch: Batch):
        self._saved_batches.add(batch)

    def get_batches(self) -> Iterable[Batch]:
        return self._saved_batches

    def get_batch(self, reference) -> Batch | None:
        try:
            return next(
                batch for batch in self._saved_batches if batch.reference == reference
            )
        except StopIteration:
            raise BatchNotFoundInDataException()

    def __len__(self):
        return len(self._saved_batches)
