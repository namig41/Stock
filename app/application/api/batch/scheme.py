from datetime import date
from pydantic import BaseModel

from domain.entities.batch import Batch


class GetBatchRequestScheme(BaseModel):
    reference: str
    
    
class GetBatchResponseScheme(BaseModel):
    reference: str
    sku: str
        
    @classmethod
    def from_entiry(cls, batch: Batch) -> 'GetBatchResponseScheme':
        return GetBatchResponseScheme(
            reference=batch.reference,
            sku=batch.sku,
        )

class CreateBatchRequestSchema(BaseModel):
    reference: str
    sku: str

class CreateBatchResponseScheme(BaseModel):
    reference: str
    sku: str
        
    @classmethod
    def from_entiry(cls, batch: Batch) -> 'CreateBatchResponseScheme':
        return CreateBatchResponseScheme(
            reference=batch.reference,
            sku=batch.sku
        )