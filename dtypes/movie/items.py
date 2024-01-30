
from dtypes.source import BaseSource
from utils.jsonify import Jsonified, JsonifiedProperty

from .movie_type import BaseMovieType


class BaseMovieItem(Jsonified):
    name = "base"


class PosterItem(BaseMovieItem):
    name = "poster"

    def __init__(self, height: int = None, width: int = None, url: str = None):
        self.height = height
        self.width = width
        self.url = url

        self.fields = ["height", "width", "url"]


class MovieIdItem(BaseMovieItem):
    name = "movie_id"

    def __init__(self, movie_id: str = None, source: BaseSource = BaseSource()):
        self.movie_id = movie_id
        self.source = source.name

        self.fields = ["movie_id", "source"]


class Date(BaseMovieItem):
    name = "date"

    def __init__(self, timestamp: int = None):
        self.timestamp = timestamp

        self.fields = ["timestamp"]


class AuthorItem(BaseMovieItem):
    name = "author"

    def __init__(self, first_name: str = None, surname: str = None, birthday: Date = Date()):
        self.first_name = first_name
        self.surname = surname

        self.birthday = birthday
        self.birthday.name = "birthday"

        self.fields = ["first_name", "surname", 'birthday']


class RankItem(BaseMovieItem):
    name = "rank"

    def __init__(self, position: int = None, source: BaseSource = BaseSource()):
        self.position = position
        self.source = source.name

        self.fields = ["position", "source"]


class MovieTypeItem(BaseMovieItem):
    name = "movie_type"
    type = "movie_type"

    def __init__(self, original: str = None, simple: BaseMovieType = BaseMovieType()):
        self.original = original
        self.simple = simple.name

        self.fields = ["original", "simple"]


class TitleItem(JsonifiedProperty, BaseMovieItem):
    name = "title"

    def __init__(self, title: str = None):
        self.title = title

        self.field = "title"


class TrailerItem(BaseMovieItem):
    name = "trailer"

    def __init__(self, title: TitleItem = TitleItem(), subtitle: TitleItem = TitleItem(), movie_id: MovieIdItem = MovieIdItem(), poster: PosterItem = PosterItem()):
        self.title = title
        self.subtitle = subtitle
        self.movie_id = movie_id
        self.poster = poster

        self.fields = ["title", "subtitle", "movie_id", "poster"]


class DurationItem(BaseMovieItem, JsonifiedProperty):
    name = "duration"

    def __init__(self, duration: int = None):
        self.duration = duration

        JsonifiedProperty.__init__(self, self.name, self.duration)
