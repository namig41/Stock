from fastapi import FastAPI
from application.api.batch.handlers import router as batch_router

def create_app() -> FastAPI:
    app = FastAPI(
       title='dddpy',
       docs_url='/api/docs',
       description='dddpy',
       debug=True
    )
    
    app.include_router(batch_router)
    
    return app