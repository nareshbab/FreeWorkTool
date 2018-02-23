# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from FreeWorkTool.helpers import Response
from models import User
# Create your views here.


class Login(View):

	def get(self, request):
		""

	def post(self, request):
		return Response(json.loads(request.body))

	def delete(self, request):
		""

	def put(self, request):
		""


class Logout(View):

	def get(self, request):
		""

	def post(self, request):
		""

	def delete(self, request):
		""

	def put(self, request):
		""

class Register(View):

	def post(self, request):
		payload = json.loads(request.body)
		fields = ['first_name', 'last_name', 'password', 'email']
		if all (_k in payload for _k in fields):
			User(**payload).save()
			return Response({'status': 'success', 'message': 'User created', 'redirect': '/login'})
		else:
			return Response({'status': 'ERROR', 'message': 'Required fields missing in payload'})
	
	