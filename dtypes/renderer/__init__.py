
from typing import Type, Any
import inspect

from utils.jsonify import Jsonified
from .result import DataRenderResult, RenderedData


class DataRender:
    name: str = None
    renderers: object = None
    export_key: str = "value"
    export_obj: Type[Jsonified] = RenderedData

    def __init__(self, data):
        self.export_key = self.export_key if self.export_key else self.name
        self.data = data

    def _render(self) -> DataRenderResult:
        pass

    def render(self) -> RenderedData:
        pass


class BaseDataRender(DataRender):

    def __init__(self, *args, default_key: str = None, **kwargs):
        DataRender.__init__(self, *args, **kwargs)
        self.renderers = inspect.getmodule(self) if self.renderers is None else self.renderers
        self.default_key = default_key

    def _render(self, key, value) -> DataRenderResult:
        from .utils import to_data_render
        data_render = to_data_render(key, value, self.renderers)

        if data_render is None:
            return

        return DataRenderResult(
            data_render.export_key,
            data_render.render()
        )

    def render(self) -> Type[Jsonified] | list[Type[Jsonified]] | RenderedData:
        if isinstance(self.data, list):
            export = []

            for i in self.data:
                result = self._render(self.default_key if self.default_key else self.name, i)

                if not result:
                    continue

                export.append(result.value)

        elif isinstance(self.data, dict):
            export = self.export_obj()

            for key in self.data:
                result = self._render(key, self.data[key])

                if not result:
                    continue

                export.update(**result.to_dict())

        else:
            export = {}

        return export


class BaseDataPropertyRender(DataRender):
    name: str = "base"
    export_key: str = None

    def _render(self) -> Any:
        return self.data

    def render(self) -> Any:
        return self._render()


from .imdb_search import IMDbSearchDataRender
from .utils import to_data_render
