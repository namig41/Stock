from fastapi import FastAPI
from fastapi.testclient import TestClient

import pytest
from infrastructure.container.init import init_container

from application.api.main import create_app
from tests.fixtures import init_dummy_container


@pytest.fixture
def app() -> FastAPI:
    app = create_app()
    app.dependency_overrides[init_container] = init_dummy_container

    return app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app=app)


@pytest.fixture
def url() -> str:
    return "http://127.0.0.1:8000"
