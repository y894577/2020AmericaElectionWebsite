from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.queryNews, name='queryAllNews'),
    path('<int:id>', views.queryNews, name='queryNewsById'),
    path('offset/<int:page>/<int:size>', views.queryNews, name='queryNewsList'),
    path('comment/<int:id>', views.queryComment, name='queryCommentById'),
    path('comment/<int:id>/offset/<int:page>/<int:size>', views.queryNews, name='queryCommentList'),
]
