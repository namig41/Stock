from dataclasses import dataclass, field
from datetime import date
from uuid import uuid4

from domain.value_objects.order_line import OrderLine


@dataclass
class Batch:
    oid: str = field(default_factory=lambda: str(uuid4), kw_only=True)
    reference: str
    sku: str
    eta: date = field(default_factory=date.today(), kw_only=True)
    _purchased_quantity: int = field(default_factory=0)
    _allocations: set[OrderLine] = field(default_factory=set[OrderLine])
    
    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'Batch') -> bool:
        return self.oid == __value.oid

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        for line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self._purchased_quantity >= line.qty

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta
