
from typing import Type

from utils import get_class_children
from dtypes.source import BaseSource
from . import search
from . import BaseSearch


def to_search(source_type: Type[BaseSource]) -> Type[BaseSearch] | None:
    children = get_class_children(BaseSearch, search, lambda x: issubclass(x.source.__class__, source_type.__class__))
    return None if len(children) == 0 else children[0]()
