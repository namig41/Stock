from datetime import date

from infrastructure.repository.base import BaseBatchRepository
from punq import Container

from domain.entities.batch import Batch


def test_memory_repository_add_batches(container: Container):
    batch1 = Batch("batch-001", "SMALL-TABLE", _purchased_quantity=20, eta=date.today())
    batch2 = Batch("batch-002", "SMALL-TABLE", _purchased_quantity=20, eta=date.today())

    batch_repository: BaseBatchRepository = container.resolve(BaseBatchRepository)

    batch_repository.add_batch(batch1)
    batch_repository.add_batch(batch2)

    assert len(batch_repository) == 2
    assert batch1 == batch_repository.get_batch(batch1.reference)
    assert batch2 == batch_repository.get_batch(batch2.reference)
