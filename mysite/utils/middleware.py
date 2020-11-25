import json

from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.db.models.base import *
from django.conf import settings


class middleware(MiddlewareMixin):

    # def process_request(self, request):
    #     if settings.USER_LOGIN_SESSION in request.session:
    #         pass
    #     else:
    #         data = {
    #             'status': 200,
    #             'code': 0,
    #             'msg': '用户未登录'
    #         }
    #         return JsonResponse(data)

    def process_exception(self, request, exception):
        print()
        if isinstance(exception, ObjectDoesNotExist):
            msg = '查找对象不存在'
            code = -1
        elif isinstance(exception, FieldDoesNotExist):
            msg = '查询参数有误'
            code = -2
        else:
            code = exception.args[0]
            msg = exception.args[1]
        data = {
            'status': 200,
            'code': code,
            'msg': msg
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
