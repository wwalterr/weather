from httpx import get, HTTPStatusError

from fastapi import HTTPException

SOURCE = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded'


async def extract_file(id: str, key: str) -> dict:
    try:
        response = get(f'{SOURCE}/{id}.TXT')

        response.raise_for_status()
    except HTTPStatusError as error:
        raise HTTPException(status_code=error.response.status_code, detail='Error while requesting document')

    lines = [line.split(':', 1) for line in response.text.splitlines()]
    
    match = filter(lambda line: key.lower() in next(iter(line)).lower(), lines)

    return dict(match)
