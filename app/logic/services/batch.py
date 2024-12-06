from infrastructure.uow.base import BaseUnitOfWork

from domain.entities.batch import Batch
from domain.value_objects.order_line import OrderLine


def add_batch(reference: str, sku: str, uow: BaseUnitOfWork) -> None:
    with uow:
        uow.batches_repository.add_batch(Batch(reference=reference, sku=sku))
        uow.commit()


def allocate(orderid: str, sku: str, qty: int, uow: BaseUnitOfWork) -> OrderLine:
    line: OrderLine = OrderLine(ordrid=orderid, sku=sku, qty=qty)

    with uow:
        uow.commit()

    return line
