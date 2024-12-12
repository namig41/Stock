from fastapi import FastAPI

import uvicorn
from sqlalchemy import Engine

from application.api.batch.handlers import router as batch_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="StockAPI",
        docs_url="/api/docs",
        description="API для работы с продуктом",
        debug=True,
    )

    app.include_router(batch_router)

    return app


if __name__ == "__main__":
    from infrastructure.container.init import init_container
    from infrastructure.database.models import create_database

    container = init_container()

    # Инициализация базы данных
    engine = container.resolve(Engine)
    create_database(engine)

    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
