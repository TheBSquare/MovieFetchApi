
import inspect


def get_class_children(parent: object, module, filterby=lambda x: True) -> [object]:
    members = inspect.getmembers(module)
    children = []

    for _, obj in members:
        if inspect.isclass(obj) and issubclass(obj, parent) and not isinstance(obj, parent) and filterby(obj):
            children.append(obj)

    return children
