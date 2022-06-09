from fastapi import APIRouter, status

from .utils import extract_file

router = APIRouter(
    prefix='/weather',
    tags=['weather'],
)

@router.get('/pressure', summary='Weather pressure', status_code=status.HTTP_200_OK)
async def pressure(key: str):
    return extract_file(key, 'pressure')


@router.get('/temperature', summary='Weather temperature in celsius and fahrenheit', status_code=status.HTTP_200_OK)
async def temperature(key: str):
    return extract_file(key, 'temperature')
