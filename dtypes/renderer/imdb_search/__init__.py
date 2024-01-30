
from dtypes.renderer import BaseDataRender
from . import imdb_search


class IMDbSearchDataRender(BaseDataRender):
    name = "IMDb"
    renderers = imdb_search
