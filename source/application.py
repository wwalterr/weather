from fastapi import FastAPI, Request

from .weather.router import router as weather_router

application = FastAPI(
    title='Zapata',
    description='Weather API',
    version='1.0.0'
)

application.include_router(weather_router)


@application.exception_handler(ValueError)
async def exception_handler(request: Request, exception: ValueError) -> dict:
    return {'code': status.HTTP_400_BAD_REQUEST, 'content': {'message': str(exception)}}
