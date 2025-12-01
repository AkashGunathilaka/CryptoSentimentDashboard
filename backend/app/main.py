from fastapi import FastAPI
from ..routers import health
from .core.config import settings

def create_app() -> FastAPI:
    app = FastAPI( title=settings.APP_NAME, version=settings.APP_VERSION )
    #register routers
    app.include_router(health.router)
    return app
app = create_app()
