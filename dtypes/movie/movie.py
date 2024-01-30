
from utils.jsonify import Jsonified
from .items import PosterItem, MovieIdItem, Date, AuthorItem, RankItem, MovieTypeItem, TrailerItem, TitleItem


class Movie(Jsonified):
    def __init__(
            self,
            movie_id: MovieIdItem = MovieIdItem(),
            movie_type: MovieTypeItem = MovieTypeItem(),
            title: TitleItem = TitleItem(),
            subtitle: TitleItem = TitleItem(),
            poster: PosterItem = PosterItem(),
            release: Date = Date(),
            author: AuthorItem = AuthorItem(),
            rank: RankItem = RankItem(),
            trailer: TrailerItem = TrailerItem()
    ):
        self.movie_id = movie_id
        self.movie_type = movie_type
        self.title = title
        self.subtitle = subtitle
        self.subtitle.name = "subtitle"
        self.poster = poster
        self.release = release
        self.release.name = "release"
        self.author = author
        self.rank = rank
        self.trailer = trailer

        self.fields = ["movie_id", "movie_type", "title", "subtitle", "poster", "release", "author", "rank", "trailer"]
