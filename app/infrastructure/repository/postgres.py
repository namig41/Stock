from dataclasses import dataclass
from domain.entities.batch import Batch
from infrastructure.repository.base import BaseRepository

@dataclass
class PostgresBatchRepository(BaseRepository):
    def add_batch(self, batch: Batch):
        ...
    
    def get_batch(self, reference) -> Batch:
        ...