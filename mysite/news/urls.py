from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^search/(?P<keyword>[\w-]+)/$', views.queryNews, name='queryNewsByCondition'),
    re_path(r'^search/(?P<keyword>[\w-]+)/offset/(?P<page>[1-9]|[1-9]\d*)/(?P<size>[1-9]|[1-9]\d*)/$',
            views.queryNews, name='queryNewsByKeyword'),
    re_path(r'^(?P<id>[\w-]+)/$', views.queryNews, name='queryNewsById'),
    re_path(r'^offset/(?P<page>[1-9]|[1-9]\d*)/(?P<size>[1-9]|[1-9]\d*)/$',
            views.queryNews, name='queryNewsList'),
    path('<str:id>/comment', views.queryComment, name='queryCommentById'),
    re_path(r'^(?P<id>[\w-]+)/comment/offset/(?P<page>[1-9]|[1-9]\d*)/(?P<size>[1-9]|[1-9]\d*)/$',
            views.queryComment, name='queryCommentList'),
]
