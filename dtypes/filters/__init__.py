
from typing import Type
from utils.jsonify import Jsonified


class BaseFilter:

    def __init__(self, limit=5):
        self.limit = limit

    def _process(self, row: Type[Jsonified]):
        return row

    def process(self, data: list[Type[Jsonified]]):
        return [row for row in data if self._process(row)][:self.limit]


class SearchFilter(BaseFilter):
    def __init__(self, limit, movie_type):
        BaseFilter.__init__(self, limit)
        self.movie_type = movie_type

    def _process(self, row: Type[Jsonified]):
        pass
