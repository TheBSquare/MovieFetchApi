
from typing import Type
from utils.jsonify import Jsonified
from dtypes.renderer import BaseDataRender
from dtypes.source import BaseSource
from dtypes.response import BaseResponse, OkResponse


class BaseSearch:
    source = BaseSource()
    renderer = BaseDataRender

    def __init__(self):
        self.query = None
        self.filters = None
        self.data = None

    def apply(self, query: str, filters: dict = {}):
        self.query = query
        self.filters = filters

    def _search(self) -> BaseResponse:
        pass

    def search(self) -> BaseResponse:
        if None in [self.query, self.filters]:
            return None

        response = self._search()
        if response.is_ok():
            handler = self.renderer(response.data)
            self.data = handler.render().result

        return response

    def filter(self) -> Type[Jsonified]:
        export = []

        for movie in self.data:
            if not movie.movie_type.simple:
                continue

            if self.filters['type'] == "any":
                pass

            elif movie.movie_type.simple != self.filters['type']:
                continue

            export.append(movie)

        return OkResponse(description="чунга чанга", data=export[:self.filters['amount']])

    def extract(self):
        pass


from .search import IMDbSearch
from .utils import to_search
