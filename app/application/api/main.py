from fastapi import FastAPI

import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator

from application.api.batch.handlers import router as batch_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="StockAPI",
        docs_url="/api/docs",
        description="API для работы с продуктом",
        debug=True,
    )

    app.include_router(batch_router)

    Instrumentator().instrument(app).expose(app)

    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
