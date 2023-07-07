from django.db import models

# Create your models here.

class Player(models.Model):
    PlayerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=1000)
    TeamName = models.CharField(max_length=1000)
    FantasyPoints = models.DecimalField(default=0, decimal_places=1, max_digits=10)