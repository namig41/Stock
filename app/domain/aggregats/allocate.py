from typing import List
from domain.entities.batch import Batch
from domain.value_objects.order_line import OrderLine


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    batch = next(b for b in sorted(batches) if b.can_allocate(line))
    batch.allocate(line)
    return batch.reference
