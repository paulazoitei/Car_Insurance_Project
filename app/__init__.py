from fastapi import FastAPI
from app.api.routers import health
def create_app()->FastAPI:
    app=FastAPI()
    app.include_router(health.router)

    return app

