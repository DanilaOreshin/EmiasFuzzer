import json

from utils.config import omsNumber, birthDate, specialityId, jsonrpc
from utils.util import get_uuid


class Body:
    jsonrpc: str
    id: str
    method: str
    params: dict

    def __init__(self, method):
        params = {
            "omsNumber": omsNumber,
            "birthDate": birthDate,
            "specialityId": specialityId
        }
        self.jsonrpc = jsonrpc
        self.id = get_uuid()
        self.method = method
        self.params = params

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
