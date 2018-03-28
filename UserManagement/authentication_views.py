# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from FreeWorkTool.helpers import Response
from models import User
# Create your views here.

class Name(View):

    def get(self, request):
        return {'content':'hi your name is '+request.user['first_name']}

class Login(View):

    def get(self, request):
        return request.user

    def post(self, request):
        body = request.json_body
        user = list(User.objects.raw(
            {'email': body['email'], 'password': body['password']}))
        if user:
            user = user[0]
            request.session['user'] = user.email
            return {'status': 'status'}
        return {'status': 'failure'}, 401

    def delete(self, request):
        ""

    def put(self, request):
        ""


class Logout(View):

    def get(self, request):
        ""

    def post(self, request):
    	del request.session['user']
    	return {'status':'success'}

    def delete(self, request):
        ""

    def put(self, request):
        ""


class Register(View):

    def post(self, request):
        payload = json.loads(request.body)
        fields = ['first_name', 'last_name', 'password', 'email']
        if all(_k in payload for _k in fields):
            User(**payload).save()
            return Response({'status': 'success', 'message': 'User created', 'redirect': '/login'})
        else:
            return Response({'status': 'ERROR', 'message': 'Required fields missing in payload'})
