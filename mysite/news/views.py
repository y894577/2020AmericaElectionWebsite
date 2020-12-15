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
        comments = Comment.objects.order_by('-time').filter(news_id=id)[
                   (page - 1) * size:page * size].values(
            'news_id', 'time', 'content')
    except (ObjectDoesNotExist, IndexError):
        raise UtilException(code=-1, msg='获取Comment失败')
    else:
        data = {
            'status': 200,
            'code': 1,
            'msg': '获取Comment成功',
            'data': list(comments)
        }
    return JsonResponse(data)


@require_http_methods(["POST"])
def comment(request):
    content = request.POST.get('content')
    news_id = request.POST.get('news_id')
    try:
        news = News.objects.get(id=news_id)
    except Exception:
        raise UtilException(code=-1, msg='该新闻不存在')
    else:
        try:
            comments = Comment(content=content, news_id=news)
            comments.save(force_insert=True)
        except Exception:
            raise UtilException(code=-1, msg='提交Comment失败')
    data = {
        'status': 200,
        'code': 1,
        'msg': '提交Comment成功',
        'data': model_to_dict(comments)
    }
    return JsonResponse(data)
