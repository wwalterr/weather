from pytest import mark

from httpx import AsyncClient

from source.application import application

BASE_URL = 'http://localhost:4000'


@mark.parametrize(
    'key, result',
    [
        ('AABP', { 'Pressure (altimeter)': ' 29.77 in. Hg (1008 hPa)' }),
        ('AGGC', { 'Pressure (altimeter)': ' 29.80 in. Hg (1009 hPa)' })
    ]
)
@mark.asyncio
async def test_pressure(key: str, result: dict):
    async with AsyncClient(app=application, base_url=BASE_URL) as client:
        response = await client.get(f'/weather/pressure/{key}')

    assert response.status_code == 200

    assert response.json() == result


@mark.parametrize(
    'key, result',
    [
        ('AABP', { 'Temperature': ' 75 F (24 C)' }),
        ('AGGC', { 'Temperature': ' 84 F (29 C)' })
    ]
)
@mark.asyncio
async def test_temperature(key: str, result: dict):
    async with AsyncClient(app=application, base_url=BASE_URL) as client:
        response = await client.get(f'/weather/temperature/{key}')

    assert response.status_code == 200

    assert response.json() == result


@mark.parametrize(
    'url',
    [
        '/weather/pressure/',
        '/weather/temperature/'
    ]
)
@mark.asyncio
async def test_failure(url: str):
    async with AsyncClient(app=application, base_url=BASE_URL) as client:
        response = await client.get(url)

    assert response.status_code == 404
