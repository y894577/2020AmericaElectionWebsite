from django.db import models


class News(models.Model):
    title = models.CharField
    author = models.CharField
    content = models.TextField
    time = models.TimeField


class Comment(models.Model):
    user_id = models.ForeignKey(to='user.User', on_delete=models.CASCADE)
    news_id = models.ForeignKey(to='user.User', on_delete=models.CASCADE)
    time = models.TimeField
    content = models.CharField(max_length=100)
