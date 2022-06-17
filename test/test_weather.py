from pytest import mark

from httpx import AsyncClient

from source.application import application

# Create a cache instance if the tests are running
# without having one already created by the Docker
# Compose:
#
# docker run -it -d --name cache -e ALLOW_EMPTY_PASSWORD='yes' -p 6379:6379 redis:7.0.2-alpine # container name and image name

BASE_URL = 'http://localhost:4000'


@mark.parametrize(
    argnames='id, result',
    argvalues=[
        ('AABP', '"29.77 in. Hg (1008 hPa)"'),
        ('AGGC', '"29.80 in. Hg (1009 hPa)"')
    ]
)
@mark.asyncio
async def test_pressure(id: str, result: str):
    async with AsyncClient(app=application, base_url=BASE_URL) as client:
        response = await client.get(url=f'/weather/pressure/{id}')

    assert response.status_code == 200

    assert response.text == result


@mark.parametrize(
    argnames='id, result',
    argvalues=[
        ('AABP', '"75 F (24 C)"'),
        ('AGGC', '"84 F (29 C)"')
    ]
)
@mark.asyncio
async def test_temperature(id: str, result: str):
    async with AsyncClient(app=application, base_url=BASE_URL) as client:
        response = await client.get(url=f'/weather/temperature/{id}')

    assert response.status_code == 200

    assert response.text == result


@mark.parametrize(
    argnames='url',
    argvalues=[
        '/weather/pressure/',
        '/weather/temperature/'
    ]
)
@mark.asyncio
async def test_failure(url: str):
    async with AsyncClient(app=application, base_url=BASE_URL) as client:
        response = await client.get(url=url)

    assert response.status_code == 404
