from utils.jsonify import Jsonified


class DataRenderResult:
    def __init__(self, key: str = None, value: object = None):
        self.key = key
        self.value = value

    def to_dict(self):
        return {
            "key": self.key,
            "value": self.value
        }


class RenderedData(Jsonified):
    def __init__(self):
        self.result = None
        self.fields = ["result"]
