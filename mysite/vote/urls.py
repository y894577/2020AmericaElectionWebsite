from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/state', views.getStateList, name='getStateList'),
]
