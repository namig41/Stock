from typing import Iterable

from pydantic import BaseModel

from domain.entities.batch import Batch


class GetBatchRequestSchema(BaseModel):
    reference: str


class GetBatchResponseSchema(BaseModel):
    reference: str
    sku: str

    @classmethod
    def from_entity(cls, batch: Batch) -> "GetBatchResponseSchema":
        return cls(
            reference=batch.reference,
            sku=batch.sku,
        )


class GetBatchesResponseSchema(BaseModel):
    batches: Iterable[GetBatchResponseSchema]

    @classmethod
    def from_entity(cls, batches: Iterable[Batch]) -> "GetBatchesResponseSchema":
        return cls(
            batches=[GetBatchResponseSchema.from_entity(batch) for batch in batches],
        )


class CreateBatchRequestSchema(BaseModel):
    reference: str
    sku: str


class CreateBatchResponseSchema(BaseModel):
    reference: str
    sku: str

    @classmethod
    def from_entity(cls, batch: Batch) -> "CreateBatchResponseSchema":
        return cls(
            reference=batch.reference,
            sku=batch.sku,
        )
