import datetime
from decimal import Decimal
from flask import json


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(round(obj, 18))
        if isinstance(obj, datetime.datetime):
            return obj.isoformat(timespec='microseconds')
        return super(JsonEncoder, self).default(obj)
