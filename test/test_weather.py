from pytest import mark

from fastapi.testclient import TestClient

from source.application import application

client = TestClient(application)


@mark.parametrize(
    'key, result',
    [
        ('AABP', { 'Pressure (altimeter)': ' 29.77 in. Hg (1008 hPa)' }),
        ('AGGC', { 'Pressure (altimeter)': ' 29.80 in. Hg (1009 hPa)' })
    ]
)
def test_pressure(key: str, result: dict):
    response = client.get(f'/weather/pressure/{key}')

    assert response.status_code == 200

    assert response.json() == result


@mark.parametrize(
    'key, result',
    [
        ('AABP', { 'Temperature': ' 75 F (24 C)' }),
        ('AGGC', { 'Temperature': ' 84 F (29 C)' })
    ]
)
def test_temperature(key: str, result: dict):
    response = client.get(f'/weather/temperature/{key}')

    assert response.status_code == 200

    assert response.json() == result


@mark.parametrize(
    'url',
    [
        '/weather/pressure/',
        '/weather/temperature/'
    ]
)
def test_failure(url: str):
    response = client.get(url)

    assert response.status_code == 404
