import asyncio
import re

import aiohttp
import requests
import base64
from urllib.parse import unquote
from bs4 import BeautifulSoup


from StreamDownloader.settings import VOIDBOOST_ROOT
from StreamDownloader.utils.settings import get_settings
from StreamDownloader.db import Db
from StreamDownloader.utils import prepare_streams


async def get_series_query(base_link, token, season):
    if not isinstance(season, (int, str)):
        raise TypeError('The season argument must be type str that contains number -> "123" or int')

    if not isinstance(base_link, str):
        raise TypeError('The imdb_link argument must be type str')

    try:
        season = int(season)
    except ValueError as err:
        raise ValueError('The season argument must be type str that contains number -> "123"')

    if season < 1:
        raise ValueError("The season number must be higher than 0")

    if not base_link.startswith("https://voidboost.tv/embed/") and not base_link.startswith("https://voidboost.tv/serial/"):
        raise ValueError(f'The imdb link have to starts with "https://voidboost.tv/embed/"')

    base_link = base_link.replace("token", token)
    imdb_link = "".join((base_link, f"?s={season}&e=1&h=gidonline.io"))

    async with aiohttp.ClientSession() as session:
        async with session.get(imdb_link) as response:
            content = await response.text()
            soup = BeautifulSoup(content, "html.parser")
            episodes = [option["value"] for option in soup.select('select[name="episode"] option')]

            return {token: {season: [''.join((base_link, f"?s={season}&e={episode}&h=gidonline.io")) for episode in episodes]}}


async def async_process(data):
    tasks = [get_series_query(url, token, season) for url, token, season in data]
    results = await asyncio.gather(*tasks)
    return results


def get_embeds(imdb_link, content):
    _filter = ["", None]

    if not isinstance(imdb_link, str):
        raise TypeError('The imdb_link argument must be type str')

    if not isinstance(content, (bytes, str)):
        raise TypeError("The content argument must be type str or bytes")

    if not imdb_link.startswith("https://voidboost.tv/embed/"):
        raise ValueError(f'The imdb link have to starts with "https://voidboost.tv/embed/"')

    soup = BeautifulSoup(content, "html.parser")

    translates = [option for option in soup.select('select[name="translator"] option')]
    general_seasons = [option.get("value") for option in soup.select('select[name="season"] option')]
    is_siries = len(general_seasons) > 0

    data = {}
    links = []

    for translate in translates:
        token = translate.get("data-token")
        if token in _filter:
            continue

        if not is_siries:
            data.update({token: {"name": translate.get_text(strip=True), "seasons": {1: f"{VOIDBOOST_ROOT}movie/{token}/iframe?h=gidonline.io"}}})
            continue

        data.update({token: {"name": translate.get_text(strip=True), "seasons": {}}})

        for i in general_seasons:
            links.append([f"{VOIDBOOST_ROOT}serial/token/iframe", token, i])

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    results = loop.run_until_complete(async_process(links))

    for result in results:
        translate_key = next(iter(result.keys()))
        season = result[translate_key]
        data[translate_key]["seasons"].update(season)

    return {"status": "ok", "embeds": data}


def add_embeds(embeds, imdb):
    db = Db()
    settings = get_settings()["database"]
    db.auth(**settings)
    title_id = db.get_title_id(imdb)

    if title_id is None:
        return {"status": "err", "desc": "cant find title in db"}

    return db.add_videos(embeds, db.get_title_id(imdb)[0])


def get_streams(embed):
    if not isinstance(embed, str):
        raise TypeError('The imdb_link argument must be type str')

    if not embed.startswith("https://voidboost.tv/embed/") and not embed.startswith("https://voidboost.tv/movie/") \
            and not embed.startswith("https://voidboost.tv/serial/"):
        raise ValueError(f'The imdb link have to starts with "https://voidboost.tv/embed/" or "https://voidboost.tv/movie/" or "https://voidboost.tv/serial/"')

    steps = [
        get_embed_data,
        decode_streams,
        prepare_streams
    ]

    data = {
        "embed": embed
    }

    for step in steps:
        data = step(data)
        if data["status"] != "ok":
            return data

    return data


def get_embed_data(data):
    embed = data.get("embed")
    response = requests.get(embed)

    if response.status_code != 200:
        return {"status": "err", "desc": "cant connect to embed"}

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        script = soup.select("body script")[1].get_text(strip=True)
    except Exception as err:
        return {"status": "err", "desc": "cant find script file"}

    match = re.search(r"'file'\s*:\s*'([^']+)'", script)

    try:
        return {"status": "ok", "file": match.group(1)[2:]}
    except Exception as err:
        return {"status": "err", "desc": "cant get file from embed"}


def decode_streams(data):
    if not isinstance(data, dict):
        raise TypeError("data must be type dict")

    file = data.get("file")

    if not isinstance(file, str):
        raise TypeError(f"file key must be type str not {type(file)}")

    splitters = [
        "//_//JCQkIyMjIyEhISEhISE=",
        "//_//Xl5eXl5eIyNA",
        "//_//QCFeXiFAI0BAJCQkJCQ=",
        "//_//Xl4jQEAhIUAjISQ=",
        "//_//QCMhQEBAIyMkJEBA",
    ]

    def decode(encoded_string):
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_str = "".join(["%" + format(c, '02x') for c in decoded_bytes])
        decoded_result = unquote(decoded_str)
        return decoded_result

    for splitter in splitters:
        file = file.replace(splitter, "")

    return {"status": "ok", "streams": decode(file)}


def is_voidboost_embed(embed):
    parts = ["https://voidboost.tv/embed/", "https://voidboost.tv/movie/", "https://voidboost.tv/serial/"]

    for part in parts:
        if embed.startswith(part):
            return True

    return False


if __name__ == '__main__':
    pass
