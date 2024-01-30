
from datetime import datetime

from dtypes.renderer import BaseDataRender, BaseDataPropertyRender
from dtypes.movie import Movie, PosterItem, MovieIdItem, MovieTypeItem, TitleItem, RankItem, Date, TrailerItem, to_movie_type
from dtypes.source import IMDbSource


class MovieDataRender(BaseDataRender):
    name = "d"
    export_key = "result"
    export_obj = Movie


class PosterDataRender(BaseDataRender):
    name = "i"
    export_key = "poster"
    export_obj = PosterItem


class HeightDataRender(BaseDataPropertyRender):
    name = "height"
    export_key = "height"

    def _render(self):
        return int(self.data)


class WeightDataRender(BaseDataPropertyRender):
    name = "width"
    export_key = "width"

    def _render(self):
        return int(self.data)


class ImageUrlDataRender(BaseDataPropertyRender):
    name = "imageUrl"
    export_key = "url"


class MovieIdDataRender(BaseDataPropertyRender):
    name = "id"
    export_key = "movie_id"

    def render(self):
        return MovieIdItem(
            movie_id=self.data,
            source=IMDbSource
        )


class MovieTypeRender(BaseDataPropertyRender):
    name = "qid"
    export_key = "movie_type"

    def render(self):
        return MovieTypeItem(
            original=self.data,
            simple=to_movie_type(IMDbSource(), self.data)
        )


class TitleDataRender(BaseDataPropertyRender):
    name = "l"
    export_key = "title"
    export_obj = TitleItem


class SubTitleRender(BaseDataPropertyRender):
    name = "s"
    export_key = "subtitle"
    export_obj = TitleItem


class RankRender(BaseDataPropertyRender):
    name = "rank"
    export_key = "rank"

    def render(self):
        return RankItem(
            position=int(self.data),
            source=IMDbSource()
        )


class ReleaseRender(BaseDataRender):
    name = "y"
    export_key = "release"

    def render(self):
        date = Date(
            round(datetime(int(self.data), 1, 1).timestamp())
        )
        date.name = self.export_key
        return date


class TrailerRender(BaseDataRender):
    name = "v"
    export_key = "trailer"
    export_obj = TrailerItem
