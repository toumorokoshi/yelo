from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Match(models.Model):
    winner = models.ForeignKey(User, related_name='winner')
    winner_before_elo = models.IntegerField()
    winner_after_elo = models.IntegerField()
    loser = models.ForeignKey(User, related_name='loser')
    loser_before_elo = models.IntegerField()
    loser_after_elo = models.IntegerField()
    match_date = models.DateTimeField('match date', auto_now_add=True)


class Elo(models.Model):
    elo = models.IntegerField(default=800)
    player = models.ForeignKey(User)

    def __str__(self):
        return "{0} ({1})".format(self.player, self.elo)
