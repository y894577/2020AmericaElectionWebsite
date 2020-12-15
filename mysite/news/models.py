from django.db import models
from datetime import datetime
from django.utils import timezone


class News(models.Model):
    title = models.TextField(null=True)
    author = models.CharField(max_length=60, null=True)
    content = models.TextField(null=True)
    time = models.DateTimeField(default=datetime.now)


class Comment(models.Model):
    # user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    content = models.CharField(max_length=100)

    @property
    def info(self):
        info = {
            # 'user_id': self.user_id,
            # 'user_name': self.user_id.name,
            # 'user_state': self.user_id.state.name,
            'news_id': self.news_id,
            'content': self.content,
            'time': self.time
        }
        return info
