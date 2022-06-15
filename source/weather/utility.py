from httpx import get, HTTPStatusError

from fastapi import HTTPException

from re import sub

from aioredis import from_url


SOURCE = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded'


async def scrap_document(id: str) -> dict:
    try:
        # TO DO: Filter file extension
        response = get(url=f'{SOURCE}/{id}.TXT')

        response.raise_for_status()
    except HTTPStatusError as error:
        raise HTTPException(status_code=error.response.status_code, detail='Error while requesting document')

    lines = [line.split(':', 1) for line in response.text.splitlines()]
    
    document = {}

    for line in lines[2:]:
        if len(line) == 2:
            key, value = line

            key = sub(pattern=r'[()]', repl='', string=key).replace(' ', '_').lower()

            document[key] = value.strip()
    
    return document


async def document(id: str) -> dict:
    # TO DO: Create a pool https://stackoverflow.com/a/66561434
    redis = from_url(url='redis://localhost', decode_responses=True)

    if await redis.exists(id):
        # TO DO: Expire document
        return await redis.hgetall(name=id)
    else:
        document = await scrap_document(id=id)
        
        # TO DO: Execute as a background task
        await redis.hset(name=id, mapping=document)

        return document