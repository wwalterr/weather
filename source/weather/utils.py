from typing import Dict

from requests import get

SOURCE = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded/'


def extract_file(key: str, type: str) -> Dict[str, str]:
    url = f'{SOURCE}{key}.TXT'

    text = get(url).text

    lines = [line.split(':', 1) for line in text.splitlines()]
    
    match = filter(lambda line: type.lower() in next(iter(line)).lower(), lines)

    return dict(match)
