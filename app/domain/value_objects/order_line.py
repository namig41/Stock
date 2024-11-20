from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    ordrid: str
    sku: str
    qty: int
