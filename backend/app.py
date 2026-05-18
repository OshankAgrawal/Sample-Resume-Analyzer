from fastapi import FastAPI

from api.routes import router
from src.config.app_config import AppConfig

app = FastAPI(
    title=AppConfig.API_TITLE,
    description=AppConfig.API_DESCRIPTION,
    version=AppConfig.API_VERSION
)

app.include_router(router)