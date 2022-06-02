from django.db import models


class TeamFDR(models.Model):
    name = models.CharField(max_length=100, unique=True)
    allAway = models.FloatField(default=0)
    allHome = models.FloatField(default=0)
    goalkeeperAway = models.FloatField(default=0)
    goalkeeperHome = models.FloatField(default=0)
    defenderAway = models.FloatField(default=0)
    defenderHome = models.FloatField(default=0)
    midfielderAway = models.FloatField(default=0)
    midfielderHome = models.FloatField(default=0)
    forwardAway = models.FloatField(default=0)
    forwardHome = models.FloatField(default=0)

    def __str__(self):
        return self.name
