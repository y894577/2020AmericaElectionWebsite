from django.core import serializers
from django.forms import model_to_dict
from django.views.decorators.http import require_http_methods
from .models import *
from vote.models import *
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.exceptions import *
from django.shortcuts import get_object_or_404


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
    password = make_password(password)
    try:
        user = User.objects.get(id=id, password=password)
    except ObjectDoesNotExist:
        raise Exception(-1, '登录失败')
    else:
        msg = '登录成功'
        code = 1
        user = model_to_dict(user)
        request.session[settings.USER_SESSION] = user
    data = {
        'status': 200,
        'code': code,
        'msg': msg,
        'data': user
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def logout(request):
    del request.session[settings.USER_SESSION]
    if settings.USER_SESSION in request.session:
        msg = '退出登录成功'
        code = 1
    else:
        raise Exception(-3, '退出登录失败')
    data = {
        'status': 200,
        'code': code,
        'msg': msg,
        'data': {}
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def register(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    password = request.POST.get('password')
    password = make_password(password)
    state = request.POST.get('state')
    try:
        User.objects.get(id=id)
    except ObjectDoesNotExist:
        state = State.objects.get(id=state)
        user = User(id=id, name=name, password=password, state=state)
        user.save(force_insert=True)
        msg = '注册成功'
        code = 1
    else:
        raise Exception(-3, '该用户已被注册')
    data = {
        'status': 200,
        'code': code,
        'msg': msg,
        'data': model_to_dict(user)
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def vote(request):
    print(request.session.get(settings.USER_SESSION))
    id = str(request.session.get(settings.USER_SESSION).get('id'))
    if id != request.POST.get('id'):
        raise Exception(-2, 'session与提交id不一致')
    candidate_id = request.POST.get('candidate_id')
    candidate = Candidate.objects.get(id=candidate_id)
    user = User.objects.get(id=id)
    if user.vote_candidate is not None:
        raise Exception(-3, '该用户已完成投票')
    else:
        user.vote_candidate = candidate
        user.save(force_update=True)
        state_id = str(request.session.get(settings.USER_SESSION).get('state'))
        ticket = Vote.objects.get(state_id=state_id, candidate_id=candidate_id)
        ticket.vote_num += 1
        ticket.save(force_update=True)
        msg = '投票成功'
        code = 1
        data = [model_to_dict(user), model_to_dict(ticket)][user, ticket]
    data = {
        'status': 200,
        'code': code,
        'msg': msg,
        'data': data
    }
    return JsonResponse(data)
