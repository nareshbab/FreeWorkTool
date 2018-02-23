import json
import datetime
from django.http import HttpResponse
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):

	def default(self, o):
		if isinstance(o, ObjectId):
			return o.__str__()
		elif isinstance(o, datetime.datetime):
			return o.__str__()
		else: 
			return json.JSONEncoder.encode(self, o)

class Response(HttpResponse):

	def __init__(self, _r, *args, **kwargs):
		kwargs['content_type'] = 'application/json'
		super(Response, self).__init__(*args, **kwargs)
		self.content = JSONEncoder().encode(_r)