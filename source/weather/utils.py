from requests import get

SOURCE = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded'


def extract_file(id: str, key: str) -> dict:
    text = get(f'{SOURCE}/{id}.TXT').text

    lines = [line.split(':', 1) for line in text.splitlines()]
    
    match = filter(lambda line: key.lower() in next(iter(line)).lower(), lines)

    return dict(match)
