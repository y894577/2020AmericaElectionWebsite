import json

from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin


class middleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        print(str(exception))
        data = {
            'code': -1,
            'msg': json.dumps(str(exception))
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
