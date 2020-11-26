import json

from django.core import serializers
from django.forms import model_to_dict
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.core.exceptions import *
from django.shortcuts import get_object_or_404
from utils.UtilException import UtilException
from vote.models import *
from .models import *


def user(request):
    if request.method == 'POST':
        login(request)
    if request.method == 'DELETE':
        logout(request)
    if request.method == 'PUT':
        register(request)


@require_http_methods(["POST"])
def login(request):
    id = request.POST.get('id')
    password = request.POST.get('password')
    try:
        user = User.objects.get(id=id)
    except ObjectDoesNotExist:
        raise UtilException(code=-1, msg='该用户不存在')
    else:
        if check_password(password, user.password) is False:
            raise Exception(-1, '密码有误，请重试')
        else:
            msg = '登录成功'
            code = 1
            request.session[settings.USER_SESSION] = user
    data = {
        'status': 200,
        'code': code,
        'msg': msg,
        'data': user.info
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def logout(request):
    try:
        if request.session.get(settings.USER_SESSION, False):
            del request.session[settings.USER_SESSION]
            msg = '退出登录成功'
        else:
            msg = '已退出登录'
        code = 1
    except BaseException:
        raise UtilException(code=-3, msg='退出登录失败')
    data = {
        'status': 200,
        'code': code,
        'msg': msg,
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def register(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    password = request.POST.get('password')
    password = make_password(password)
    state = request.POST.get('state')
    if User.objects.filter(id=id).count() > 0:
        raise UtilException(code=-3, msg='该用户已被注册')
    else:
        state = State.objects.get(id=state)
        user = User(id=id, name=name, password=password, state=state)
        user.save(force_insert=True)
        msg = '注册成功'
        code = 1
    data = {
        'status': 200,
        'code': code,
        'msg': msg,
        'data': user.info
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def vote(request):
    print(request.session.get(settings.USER_SESSION))
    id = str(request.session.get(settings.USER_SESSION).get('id'))
    if id != request.POST.get('id'):
        raise UtilException(code=-2, msg='session与提交id不一致')
    candidate_id = request.POST.get('candidate_id')
    try:
        candidate = Candidate.objects.get(id=candidate_id)
    except ObjectDoesNotExist:
        raise UtilException(code=-1, msg='该候选人不存在')
    user = User.objects.get(id=id)
    if user.vote_candidate is not None:
        raise UtilException(code=-3, msg='该用户已完成投票')
    else:
        user.vote_candidate = candidate
        user.save(force_update=True)
        state_id = str(request.session.get(settings.USER_SESSION).get('state'))
        ticket = Vote.objects.get(state_id=state_id, candidate_id=candidate_id)
        ticket.vote_num += 1
        ticket.save(force_update=True)
        msg = '投票成功'
        code = 1
        data = {'user': user.info, 'vote': model_to_dict(ticket)}
    data = {
        'status': 200,
        'code': code,
        'msg': msg,
        'data': data
    }
    return JsonResponse(data)
