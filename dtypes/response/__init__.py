
from utils.jsonify import Jsonified


class BaseResponse(Jsonified):
    status: str = "base"
    description: str = "base"
    data: object = dict()

    def __init__(self, description: str = None, data: object = None):
        self.status = self.status
        self.description = description if description else self.description
        self.data = data if data else self.data

        self.fields = ["status", "description", "data"]

    def is_err(self):
        return self.status == "err"

    def is_ok(self):
        return self.status == "ok"


from .response import OkResponse, ErrResponse
