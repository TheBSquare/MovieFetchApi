
from typing import Type

from dtypes.source import BaseSource, IMDbSource, VBSource
from . import BaseMovieType, SeriesType, MovieType


def to_movie_type(source_type: Type[BaseSource], original: str) -> Type[BaseMovieType]:
    original = original.lower()

    if isinstance(source_type, IMDbSource):
        if "tv" in original or "series" in original:
            return SeriesType()

        elif "movie" in original or "video" in original:
            return MovieType()

    return BaseMovieType()
