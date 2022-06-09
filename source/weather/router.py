from fastapi import APIRouter, status

from .utils import extract_file

router = APIRouter(
    prefix='/weather',
    tags=['weather'],
)


@router.get('/pressure/{id}', summary='Weather pressure', status_code=status.HTTP_200_OK)
async def pressure(id: str):
    return extract_file(id=id, key='pressure')


@router.get('/temperature/{id}', summary='Weather temperature in celsius and fahrenheit', status_code=status.HTTP_200_OK)
async def temperature(id: str):
    return extract_file(id=id, key='temperature')
