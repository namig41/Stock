from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.entities.batch import Batch

@dataclass
class BaseRepository(ABC):
    @abstractmethod
    def add_batch(self, batch: Batch):
        ...
    
    @abstractmethod
    def get_batch(self, reference: str) -> Batch:
        ...
