from fastapi.testclient import TestClient

from source.application import application

client = TestClient(application)


def test_pressure():
    response = client.get('/weather/pressure/AABP')

    assert response.status_code == 200

    assert response.json() == { 'Pressure (altimeter)': ' 29.77 in. Hg (1008 hPa)' }


def test_temperature():
    response = client.get('/weather/temperature/AABP')

    assert response.status_code == 200

    assert response.json() == { 'Temperature': ' 75 F (24 C)' }
