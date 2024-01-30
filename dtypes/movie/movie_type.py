
class BaseMovieType:
    name = "base"

    def __str__(self):
        return f"MovieType: {self.name}"


class MovieType(BaseMovieType):
    name = "movie"


class SeriesType(BaseMovieType):
    name = "series"
