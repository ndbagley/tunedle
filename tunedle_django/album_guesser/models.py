from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.TextField()
    date_used = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Guess(models.Model):
    total_guesses = models.IntegerField()
    average_guesses = models.FloatField()
    days_played = models.IntegerField()
    streak = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)