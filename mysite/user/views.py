from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import *
import json
from django.http import JsonResponse
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
    data = {
        'code': '200',
        'msg': '',
        'data': list(user)
    }
    return JsonResponse(data)


@require_http_methods(["POST"])
def logout(request):
    return


@require_http_methods(["POST"])
def register(request):
    return


@require_http_methods(["POST"])
def vote(request):
    return
