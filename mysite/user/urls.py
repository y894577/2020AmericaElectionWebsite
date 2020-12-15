from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('vote', views.vote, name='vote')
]
