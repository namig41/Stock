from fastapi import APIRouter, Depends, HTTPException, status

from application.api.batch.scheme import CreateBatchRequestSchema, CreateBatchResponseScheme, GetBatchRequestScheme, GetBatchResponseScheme
from application.exceptions.base import ApplicationException
from domain.entities.batch import Batch
from infrastructure.repository.base import BaseRepository
from infrastructure.repository.init import init_repository


router = APIRouter(
    prefix='/batch',
    tags=['Batch']
)

@router.get(
    '/{reference}',
    response_model=GetBatchResponseScheme,
    status_code=status.HTTP_200_OK,
    description='Эндпоинт для получения продукта'
)
def get_batch_by_reference(scheme: GetBatchRequestScheme = Depends(), repository: BaseRepository=Depends(init_repository)):
    try:
        batch = repository.get_batch(reference=scheme.reference)
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    
    return GetBatchResponseScheme.from_entiry(batch)

@router.post(
    '/',
    response_model=CreateBatchResponseScheme,
    status_code=status.HTTP_201_CREATED,
    description='Эндпоинт создает новый продукт'
)
def post_batch(scheme: CreateBatchRequestSchema, repository: BaseRepository=Depends(init_repository)):
    try:
        repository.add_batch(Batch(reference=scheme.reference, sku=scheme.sku))
        batch = repository.get_batch(reference=scheme.reference)
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    
    return CreateBatchResponseScheme.from_entiry(batch)
    