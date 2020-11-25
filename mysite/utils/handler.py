import json
import traceback

from django.http import HttpResponse


def server_error(request):
    data = {
        'status': 500,
        'msg': '500 server error'
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def page_not_found(request, exception):
    print(exception)
    data = {
        'status': 404,
        'msg': '404 not found'
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def bad_request(request, exception):
    data = {
        'status': 400,
        'msg': '400 bad request'
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def permission_denied(request, exception):
    print(exception)
    data = {
        'status': 403,
        'msg': '403 permission denied'
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
