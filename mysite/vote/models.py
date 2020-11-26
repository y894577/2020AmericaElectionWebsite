from django.db import models


# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=20)
    introduction = models.TextField()
    information = models.TextField()
    party = models.CharField(max_length=20)


class State(models.Model):
    name = models.CharField(max_length=40)

    def info(self):
        return {id: self.id, name: self.name}


class Vote(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    vote_num = models.IntegerField(default=0)
