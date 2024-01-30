
class BaseSource:
    name = "base"

    def __str__(self):
        return f"SourceObject: {self.name}"


from .source import IMDbSource, VBSource
from .utils import to_source
