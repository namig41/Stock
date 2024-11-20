from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from infrastructure.repository.base import BaseRepository
from infrastructure.repository.init import init_repository

from application.api.batch.schema import (
    CreateBatchRequestSchema,
    CreateBatchResponseSchema,
    GetBatchResponseSchema,
)
from application.exceptions.base import ApplicationException
from domain.entities.batch import Batch


router = APIRouter(
    prefix="/batch",
    tags=["Batch"],
)


@router.get(
    "/{reference}",
    response_model=GetBatchResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Эндпоинт для получения продукта",
)
def get_batch_by_reference(
    reference: str,
    repository: BaseRepository = Depends(init_repository),
):
    try:
        batch = repository.get_batch(reference=reference)
    except ApplicationException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": exception.message},
        )

    return GetBatchResponseSchema.from_entiry(batch)


@router.post(
    "/",
    response_model=CreateBatchResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description="Эндпоинт создает новый продукт",
)
def post_batch(
    schema: CreateBatchRequestSchema,
    repository: BaseRepository = Depends(init_repository),
):
    try:
        repository.add_batch(Batch(reference=schema.reference, sku=schema.sku))
        batch = repository.get_batch(reference=schema.reference)
    except ApplicationException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": exception.message},
        )

    return CreateBatchResponseSchema.from_entiry(batch)
