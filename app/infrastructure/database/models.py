from sqlalchemy import (
    Column,
    Date,
    Engine,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy.orm import (
    registry,
    relationship,
)

from domain.entities.batch import Batch
from domain.value_objects.order_line import OrderLine


mapper_registry = registry()
metadata = mapper_registry.metadata

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("qty", Integer),
    Column("orderid", String(255)),
)

batches = Table(
    "batches",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reference", String(255)),
    Column("sku", String(255)),
    Column("_purchased_quantity", Integer),
    Column("eta", Date),
)

allocations = Table(
    "allocations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("orderline_id", ForeignKey("order_lines.id")),
    Column("batch_id", ForeignKey("batches.id")),
)


def start_mappers() -> None:
    mapper_registry.map_imperatively(OrderLine, order_lines)
    mapper_registry.map_imperatively(
        Batch,
        batches,
        properties={
            "_allocations": relationship(
                OrderLine,
                secondary=allocations,
                collection_class=set,
            ),
        },
    )


def create_database(engine: Engine):
    metadata.create_all(engine)
    start_mappers()
