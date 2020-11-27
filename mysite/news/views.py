import json

from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.decorators.http import require_http_methods
from django.core.exceptions import *
from django.db.models import F, Q
from utils.UtilException import UtilException
from .models import *


@require_http_methods(["GET"])
def queryNews(request, id=None, keyword=None, page=1, size=20):
    page = int(page)
    size = int(size)
    try:
        if id is not None:
            news = model_to_dict(News.objects.get(id=id))
        elif keyword is not None:
            news = list(News.objects.order_by('-time')
                        .filter(Q(title__contains=keyword) | Q(content__contains=keyword))
                        .values()[(page - 1) * size:page * size])
        else:
            news = list(News.objects.values()[(page - 1) * size:page * size])
    except (ObjectDoesNotExist, IndexError):
        raise UtilException(code=-1, msg='获取News失败')
    else:
        data = {
            'status': 200,
            'code': 1,
            'msg': '获取News成功',
            'data': news
        }
    return JsonResponse(data)


@require_http_methods(["GET"])
def queryComment(request, id=None, page=1, size=20):
    page = int(page)
    size = int(size)
    try:
        comment = Comment.objects.order_by('-time').select_related('user_id').filter(news_id=id)[
                  (page - 1) * size:page * size].values(
            'news_id', 'time', 'content', 'user_id', user_name=F('user_id__name'), user_state=F('user_id__state__name'))
    except (ObjectDoesNotExist, IndexError):
        raise UtilException(code=-1, msg='获取Comment失败')
    else:
        data = {
            'status': 200,
            'code': 1,
            'msg': '获取Comment成功',
            'data': list(comment)
        }
    return JsonResponse(data)
