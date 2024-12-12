from infrastructure.uow.base import BaseUnitOfWork

from domain.entities.batch import Batch


def add_batch(reference: str, sku: str, uow: BaseUnitOfWork) -> None:
    with uow:
        uow.batches_repository.add_batch(Batch(reference=reference, sku=sku))
        uow.commit()
