from typing import Iterable

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from infrastructure.container.init import init_container
from infrastructure.repository.base import BaseBatchRepository
from punq import Container

from application.api.batch.schema import (
    CreateBatchRequestSchema,
    CreateBatchResponseSchema,
    GetBatchesResponseSchema,
    GetBatchResponseSchema,
)
from application.exceptions.base import ApplicationException
from domain.entities.batch import Batch


router = APIRouter(
    prefix="/batches",
    tags=["Batch"],
)


@router.get(
    "/",
    response_model=GetBatchesResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Эндпоинт для получения всех продуктов",
)
def get_batches(
    container: Container = Depends(init_container),
) -> GetBatchesResponseSchema:
    try:
        batch_repository: BaseBatchRepository = container.resolve(BaseBatchRepository)
        batches: Iterable[Batch] = batch_repository.get_batches()
    except ApplicationException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        )
    return GetBatchesResponseSchema.from_entity(batches)


@router.get(
    "/{reference}",
    response_model=GetBatchResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Эндпоинт для получения продукта",
)
def get_batch_by_reference(
    reference: str,
    container: Container = Depends(init_container),
) -> GetBatchResponseSchema:
    try:
        batch_repository: BaseBatchRepository = container.resolve(BaseBatchRepository)
        batch: Batch = batch_repository.get_batch(reference=reference)
    except ApplicationException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        )
    return GetBatchResponseSchema.from_entity(batch)


@router.post(
    "/",
    response_model=CreateBatchResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description="Эндпоинт создает новый продукт",
)
def post_batch(
    schema: CreateBatchRequestSchema,
    container: Container = Depends(init_container),
) -> CreateBatchResponseSchema:
    try:
        batch_repository: BaseBatchRepository = container.resolve(BaseBatchRepository)
        batch_repository.add_batch(Batch(reference=schema.reference, sku=schema.sku))
        batch: Batch = batch_repository.get_batch(reference=schema.reference)
    except ApplicationException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        )

    return CreateBatchResponseSchema.from_entity(batch)
