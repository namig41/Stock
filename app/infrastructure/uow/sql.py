from dataclasses import (
    dataclass,
    field,
)

from infrastructure.database.init import engine
from infrastructure.repository.base import BaseBatchRepository
from infrastructure.repository.postgres import PostgreSQLBatchRepository
from infrastructure.uow.base import BaseUnitOfWork
from sqlalchemy.orm import sessionmaker


@dataclass
class SqlAlchemyUnitOfWork(BaseUnitOfWork):

    batches_repository: BaseBatchRepository = field(
        default_factory=lambda: PostgreSQLBatchRepository(),
    )
    session_factory: sessionmaker = field(
        default_factory=lambda: sessionmaker(bind=engine),
    )

    def __enter__(self):
        self.session = self.session_factory()
        self.batches = PostgreSQLBatchRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
