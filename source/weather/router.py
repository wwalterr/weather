from fastapi import APIRouter, status

from .utility import document

router = APIRouter(
    prefix='/weather',
    tags=['weather'],
)


@router.get('/pressure/{id}', summary='Weather pressure from altimeter', status_code=status.HTTP_200_OK)
async def pressure(id: str):
    return (await document(id=id)).get('pressure_altimeter', '')


@router.get('/temperature/{id}', summary='Weather temperature in celsius and fahrenheit', status_code=status.HTTP_200_OK)
async def temperature(id: str):
    return (await document(id=id)).get('temperature', '')
