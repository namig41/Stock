from dataclasses import dataclass
from typing import Iterable

from infrastructure.database.init import engine
from infrastructure.repository.base import BaseBatchRepository
from infrastructure.repository.converter import convert_batch_data_to_entity
from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.entities.batch import Batch


@dataclass
class PostgreSQLBatchRepository(BaseBatchRepository):
    def add_batch(self, batch: Batch):
        with Session(engine) as session:
            session.add(batch)
            session.commit()

    def get_batches(self) -> Iterable[Batch]:
        with Session(engine) as session:
            query = select(Batch)
            batch_data: dict = session.scalar(query)
            batch: Batch = convert_batch_data_to_entity(batch_data)
            return batch

    def get_batch(self, reference: str) -> Batch:
        with Session(engine) as session:
            query = select(Batch).where(Batch.reference == reference)
            batch_data: dict = session.scalar(query)
            batch: Batch = convert_batch_data_to_entity(batch_data)
            return batch
