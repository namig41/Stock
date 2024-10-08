from datetime import date
import pytest

from domain.entities.batch import Batch
from infrastructure.repository.memory import MemoryBatchRepository
from infrastructure.repository.sqlite import SQLiteBatchRepository

def test_memory_repository_add_batches():
    batch1 = Batch("batch-001", "SMALL-TABLE", _purchased_quantity=20, eta=date.today())
    batch2 = Batch("batch-002", "SMALL-TABLE", _purchased_quantity=20, eta=date.today())

    rep = MemoryBatchRepository()
    
    rep.add_batch(batch1)
    rep.add_batch(batch2)
    
    assert batch1 == rep.get_batch(batch1.reference)
    

def test_sql_repository_add_batches():
    batch1 = Batch("batch-001", "SMALL-TABLE", _purchased_quantity=20, eta=date.today())
    batch2 = Batch("batch-002", "SMALL-TABLE", _purchased_quantity=20, eta=date.today())

    rep = SQLiteBatchRepository('app/infrastructure/db/db')
    
    rep.add_batch(batch1)
    rep.add_batch(batch2)
    
    assert batch1 == rep.get_batch(batch1.reference)