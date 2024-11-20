from dataclasses import dataclass

from infrastructure.repository.base import BaseRepository

from domain.entities.batch import Batch


@dataclass
class PostgresBatchRepository(BaseRepository):
    def add_batch(self, batch: Batch): ...

    def get_batch(self, reference: str) -> Batch:
        return Batch()
