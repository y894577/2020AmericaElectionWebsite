from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from user.models import User
from django.views.decorators.http import require_http_methods
from django.conf import *
from .models import State, Candidate, Vote
import json


@require_http_methods(["GET"])
def queryState(request, id=None):
    if id is not None:
        state = model_to_dict(State.objects.get(id=id))
    else:
        state = list(State.objects.values())
    data = {
        'status': '200',
        'code': 1,
        'msg': '获取State信息成功',
        'data': state
    }
    return JsonResponse(data)


@require_http_methods(["GET"])
def queryCandidate(request, id=None):
    if id is not None:
        candidate = model_to_dict(Candidate.objects.get(id=id))
    else:
        candidate = list(Candidate.objects.values())
    data = {
        'status': '200',
        'code': 1,
        'msg': '获取Candidate信息成功',
        'data': candidate
    }
    return JsonResponse(data)
