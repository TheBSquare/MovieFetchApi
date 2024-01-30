
from typing import Type

from utils import get_class_children
from . import DataRender


def to_data_render(key, value, module) -> Type[DataRender] | None:
    children = get_class_children(DataRender, module, lambda x: x.name == key)
    return None if len(children) == 0 else children[0](value)
