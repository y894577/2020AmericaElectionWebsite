from django.db import models
import datetime


class News(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=20, null=True)
    content = models.TextField(null=True)
    time = models.DateTimeField(default=datetime.datetime.now())


class Comment(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now())
    content = models.CharField(max_length=100)
