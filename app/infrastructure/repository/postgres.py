from dataclasses import dataclass
from typing import Iterable

from infrastructure.repository.base import BaseBatchRepository
from sqlalchemy import (
    Engine,
    select,
)
from sqlalchemy.orm import Session

from domain.entities.batch import Batch


@dataclass
class PostgreSQLBatchRepository(BaseBatchRepository):

    engine: Engine

    def add_batch(self, batch: Batch):
        with Session(self.engine) as session:
            session.add(batch)
            session.commit()

    def get_batches(self) -> Iterable[Batch]:
        with Session(self.engine) as session:
            query = select(Batch)
            batches: Iterable[Batch] = session.scalars(query).all()
            return batches

    def get_batch(self, reference: str) -> Batch:
        with Session(self.engine) as session:
            query = select(Batch).where(Batch.reference == reference)
            batch: Batch = session.execute(query).scalar_one_or_none()

            if not batch:
                raise ValueError(f"Batch with reference {reference} not found")

            return batch
