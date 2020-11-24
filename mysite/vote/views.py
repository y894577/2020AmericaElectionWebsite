from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import State, Candidate, Vote
import json


def index(request):
    result = State.objects.values()
    data = {
        'code': '200',
        'data': list(result)
    }
    return JsonResponse(data)


def getStateList(request):
    result = State.objects.values()
    data = {
        'code': '200',
        'msg': '获取StateList成功',
        'data': list(result)
    }
    return JsonResponse(data)


def getCandidateList(request):
    result = Candidate.objects.values()
    data = {
        'code': '200',
        'msg': '获取CandidateList成功',
        'data': list(result)
    }
    return JsonResponse(data)


def queryCandidate(request):
    result = Candidate.objects.filter()

    return
