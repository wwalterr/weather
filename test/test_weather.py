from pytest import fixture, mark

from httpx import AsyncClient

from source.application import application


@fixture(autouse=True)
def settings():
    return {'base_url': 'http://localhost:4000'}


@mark.parametrize(
    argnames='id, result',
    argvalues=[
        ('AABP', '"29.77 in. Hg (1008 hPa)"'),
        ('AGGC', '"29.80 in. Hg (1009 hPa)"')
    ]
)
@mark.asyncio
async def test_pressure(settings: dict, id: str, result: str):
    async with AsyncClient(app=application, base_url=settings.get('base_url')) as client:
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
async def test_temperature(settings: dict, id: str, result: str):
    async with AsyncClient(app=application, base_url=settings.get('base_url')) as client:
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
async def test_failure(settings: dict, url: str):
    async with AsyncClient(app=application, base_url=settings.get('base_url')) as client:
        response = await client.get(url=url)

    assert response.status_code == 404
