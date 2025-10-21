from fastapi import FastAPI
from app.api.routers import health
from app.api.routers import cars
from app.api.routers import policies
def create_app()->FastAPI:
    app=FastAPI()
    app.include_router(health.router)
    app.include_router(cars.router)
    app.include_router(policies.router)

    return app

