from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import *
from vote.models import *
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password


def index(request):
    list = User.objects.all()
    data = {
        'code': '200',
        'name': json.loads(serializers.serialize('json', list, ensure_ascii=False))
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def login(request):
    id = request.POST.get("id")
    password = request.POST.get("password")
    password = make_password(password)
    user = User.objects.filter(id=id, password=password)
    if user.exists():
        msg = '登录成功'
    else:
        msg = '登录失败'
    data = {
        'code': '200',
        'msg': msg,
        'data': list(user)
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def logout(request):
    return


@require_http_methods(["POST"])
def register(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    password = request.POST.get('password')
    user = User.objects.get(id=id)
    if user:
        data = {
            'code': -1,
            'msg': '该用户已被注册',
            'data': ''
        }
    else:
        user = User(id=id, name=name, password=password)
        user.save(force_insert=True)
        data = {
            'code': 200,
            'msg': '注册成功',
            'data': json.dumps(user)
        }
        return JsonResponse(data)


@require_http_methods(["POST"])
def vote(request):
    id = request.POST.get('id')
    candidate_id = request.POST.get('candidate_id')
    user = User.objects.get(id=id)
    user.vote_candidate = candidate_id
    user.save(force_update=True)
    state_id = user.state
    ticket = Vote.objects.get(state_id=state_id, candidate_id=candidate_id)
    ticket.vote_num += 1
    ticket.save(force_update=True)
    data = {
        'code': 200,
        'msg': '投票成功',
        'data': {list(user), list(ticket)}
    }
    return JsonResponse(data)


