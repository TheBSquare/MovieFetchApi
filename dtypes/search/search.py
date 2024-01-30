import requests

from . import BaseSearch
from dtypes.renderer import IMDbSearchDataRender
from dtypes.response import ErrResponse, OkResponse
from dtypes.source import IMDbSource


class IMDbSearch(BaseSearch):
    source = IMDbSource()
    renderer = IMDbSearchDataRender

    def _search(self):
        try:
            response = requests.get(f"https://v3.sg.media-imdb.com/suggestion/x/{self.query}.json?includeVideos=1")

        except Exception as err:
            return ErrResponse(str(err))

        if response.status_code != 200:
            return ErrResponse(f"Something went wrong, status code: {response.status_code}, body: {response.text}")

        try:
            return OkResponse(data=response.json())

        except Exception as err:
            return ErrResponse(f"Cant get json from search response, body: {response.text}")
