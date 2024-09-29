from abc import abstractmethod
from dataclasses import dataclass, field
from typing import List
from domain.entities.batch import Batch
from infrastructure.repository.base import BaseRepository

@dataclass
class MemoryBatchRepository(BaseRepository):
    _saved_batches: set[Batch] = field(
        default_factory=set
    )
    
    def add_batch(self, batch: Batch):
        self._saved_batches.add(batch)
    
    def get_batch(self, reference) -> Batch | None:
        try:
            return next(
                batch for batch in self._saved_batches if batch.reference == reference
            )
        except StopIteration:
            return None
