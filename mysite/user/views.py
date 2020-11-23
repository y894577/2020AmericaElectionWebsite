from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
from django.http import JsonResponse


# Create your views here.

def index(request):
    list = User.objects.all()
    data = {
        'name': json.loads(serializers.serialize('json', list, ensure_ascii=False))
    }
    return JsonResponse(data)


def login(request):
    return
