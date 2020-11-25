import json
from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from user.models import User
from django.views.decorators.http import require_http_methods
from django.conf import *
from django.core.exceptions import *
from utils.UtilException import UtilException
from .models import State, Candidate, Vote


@require_http_methods(["GET"])
def queryState(request, id=None):
    try:
        if id is not None:
            state = model_to_dict(State.objects.get(id=id))
        else:
            state = list(State.objects.values())
    except ObjectDoesNotExist:
        raise UtilException(code=-1, msg='获取State失败')
    else:
        data = {
            'status': 200,
            'code': 1,
            'msg': '获取State成功',
            'data': state
        }
    return JsonResponse(data)


@require_http_methods(["GET"])
def queryCandidate(request, id=None):
    try:
        if id is not None:
            candidate = model_to_dict(Candidate.objects.get(id=id))
        else:
            candidate = list(Candidate.objects.values())
    except ObjectDoesNotExist:
        raise UtilException(code=-1, msg='获取Candidate失败')
    else:
        data = {
            'status': 200,
            'code': 1,
            'msg': '获取Candidate成功',
            'data': candidate
        }
    return JsonResponse(data)
