import json
from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from user.models import User
from django.views.decorators.http import require_http_methods
from django.conf import *
from django.db.models import F
from django.core.exceptions import *
from itertools import chain
from django.db.models import *
from utils.UtilException import UtilException
from .models import State, Candidate, Vote


@require_http_methods(["GET"])
def queryState(request, id=None):
    try:
        if id is not None:
            # state = model_to_dict(State.objects.get(id=id))
            state = State.objects.get(id=id)
            vote = state.vote_set.filter().values(
                'vote_num', 'candidate_id', candidate_name=F('candidate_id__name'))
            data = {'state': model_to_dict(state), 'vote': list(vote)}
        else:
            state = State.objects.all()
            vote = Vote.objects.all().values(
                'candidate_id', 'vote_num', candidate_name=F('candidate_id__name'))
            data = []
            for s in state:
                result = {
                    'state': model_to_dict(s),
                    'vote': list(vote.filter(state_id=s.id))
                }
                data.append(result)
    except ObjectDoesNotExist:
        raise UtilException(code=-1, msg='获取State失败')
    else:
        data = {
            'status': 200,
            'code': 1,
            'msg': '获取State成功',
            'data': data
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
