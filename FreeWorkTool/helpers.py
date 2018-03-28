import json
import datetime
from django.http import HttpResponse
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.__str__()
        return json.JSONEncoder.default(self, o)


class Response(HttpResponse):

    def __init__(self, _r, *args, **kwargs):
        kwargs['content_type'] = "application/json"
        super(Response, self).__init__(*args, **kwargs)
        self.content = JSONEncoder().encode(_r)
