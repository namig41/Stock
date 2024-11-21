from datetime import date

from infrastructure.repository.memory import MemoryBatchRepository
from punq import Container

from domain.entities.batch import Batch


def test_memory_repository_add_batches(container: Container):
    batch1 = Batch("batch-001", "SMALL-TABLE", _purchased_quantity=20, eta=date.today())
    batch2 = Batch("batch-002", "SMALL-TABLE", _purchased_quantity=20, eta=date.today())

    rep = MemoryBatchRepository()

    rep.add_batch(batch1)
    rep.add_batch(batch2)

    assert batch1 == rep.get_batch(batch1.reference)
