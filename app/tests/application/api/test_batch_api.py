from fastapi import FastAPI
from fastapi.testclient import TestClient

import pytest
from httpx import Response


@pytest.mark.asyncio
async def test_api_create_batch_request(
    app: FastAPI,
    client: TestClient,
    url: str,
):
    batch_data = {"reference": "batch-001", "sku": "SMALL-TABLE"}
    url = "http://127.0.0.1:8000"
    response: Response = client.post(f"{url}/batches", json=batch_data)

    assert response.is_success
    assert response.json() == batch_data


@pytest.mark.asyncio
async def test_api_get_batches_request(
    app: FastAPI,
    client: TestClient,
    url: str,
):
    response: Response = client.get(f"{url}/batches")
    assert response.is_success
