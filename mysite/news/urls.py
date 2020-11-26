from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.queryNews, name='queryAllNews'),
    path('<str:id>', views.queryNews, name='queryNewsById'),
    re_path(r'^offset/(?P<page>[1-9]|[1-9]\d*)/(?P<size>[1-9]|[1-9]\d*)/$',
            views.queryNews, name='queryNewsList'),
    path('<str:id>/comment', views.queryComment, name='queryCommentById'),
    re_path(r'^(?P<str>[\w-]+)/comment/offset/(?P<page>[1-9]|[1-9]\d*)/(?P<size>[1-9]|[1-9]\d*})/$',
            views.queryNews, name='queryCommentList'),
]
