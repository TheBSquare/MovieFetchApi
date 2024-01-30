
from typing import Type

from utils import get_class_children
from . import source
from . import BaseSource


def to_source(name: str) -> Type[BaseSource] | None:

    children = get_class_children(BaseSource, source, lambda x: x.name == name)
    return None if len(children) == 0 else children[0]()
