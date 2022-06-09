from fastapi import FastAPI

from .weather.router import router as weather_router

application = FastAPI(
    title='Zapata',
    description='Weather API',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc'
)

application.include_router(weather_router)
