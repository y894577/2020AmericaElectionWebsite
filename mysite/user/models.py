from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    vote_candidate = models.CharField(blank=True, max_length=50)
