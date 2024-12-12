from dataclasses import dataclass
from typing import Callable

from infrastructure.repository.base import BaseBatchRepository
from infrastructure.uow.base import BaseUnitOfWork
from sqlalchemy import Engine
from sqlalchemy.orm import Session


@dataclass
class UnitOfWork(BaseUnitOfWork):
    engine: Engine
    batch_repository_factory: Callable[[Session], BaseBatchRepository]

    def __enter__(self):
        self.session = Session(self.engine)
        self.batch_repository = self.batch_repository_factory(self.session)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

    def commit(self):
        if self.session:
            self.session.commit()

    def rollback(self):
        if self.session:
            self.session.rollback()
