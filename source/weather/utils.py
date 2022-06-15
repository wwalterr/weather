from requests import get, exceptions

from fastapi import HTTPException

SOURCE = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded'


def extract_file(id: str, key: str) -> dict:
    try:
        response = get(f'{SOURCE}/{id}.TXT')

        response.raise_for_status()
    except exceptions.HTTPError as error:
        raise HTTPException(status_code=404, detail='Document not found')
    except:
        raise HTTPException(status_code=500, detail='Unknown error')

    lines = [line.split(':', 1) for line in response.text.splitlines()]
    
    match = filter(lambda line: key.lower() in next(iter(line)).lower(), lines)

    return dict(match)
