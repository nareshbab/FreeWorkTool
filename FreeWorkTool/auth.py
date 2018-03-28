from UserManagement.models import User
import json
from django.http import HttpResponse
import os
from helpers import Response

def log(**kwargs):
    print '{endpoint} :: {user_id} :: {payload} :: {params} :: {browser} :: {status_code} '.format(
        **kwargs)


class AuthMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        log_body = ''
        log_params = ''
        log_user = ''
        log_endpoint = request.build_absolute_uri() + " :: " + request.method
        log_browser = request.META['HTTP_USER_AGENT']
        if request.body:
            request.json_body = json.loads(request.body)
            log_body = request.body.strip()
            log_body = log_body.replace('\n', '').replace('\t', '')
        if request.GET:
            log_params = str(dict(request.GET)).strip()
        log_args = {'endpoint': log_endpoint,
                    'user_id': log_user,
                    'payload': log_body,
                    'params': log_params,
                    'browser': log_browser}
        if not os.environ.get('local'):
            if request.session.get('user') or request.path == '/login':
            	if request.path == '/login' and request.method == 'POST':
                    log_user = request.json_body['email']
                else:
                    try:
                        user = User.objects.raw(
                            {'email': request.session.get('user')}).exclude('_cls').values()
                        user = list(user)[0]
                        request.user = user
                    except Exception as e:
                        log_args['status_code'] = 401
                        log(**log_args)
                        return HttpResponse('Error in getting auth check. Error : ' + e.message, status=401)
            else:
                log_args['status_code'] = 403
                log(**log_args)
                return HttpResponse('Auth headers missing.', status=401)

        else:
            print 'skipping auth check'
            request.user = {
                "user_id": "user_1", "remote_address": "127.0.0.1", "full_name": "Local, User"}
        if not log_user:
            log_user = request.user['user_id']
        response = self.get_response(request)
        if isinstance(response, tuple):
            log_status_code = response[1]
        else:
            log_status_code = 200
        print()
        if type(response) in [Response, HttpResponse]:
            return response
        elif isinstance(response, tuple):
            return Response(response[0], status=response[1])
        else:
            return Response(response)
