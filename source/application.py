from fastapi import FastAPI

from .weather.router import router as weather_router

application = FastAPI(
    title='Weather',
    description='Weather API',
    version='1.0.0'
)

application.include_router(weather_router)
