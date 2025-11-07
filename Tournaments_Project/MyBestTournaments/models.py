from django.db import models
from django.utils import timezone

# Create your models here.


class Games(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tournaments(models.Model):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=500)
    prize_pool = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.game.name}"


class Players(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField(max_length=500)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teams(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Players)
    country = models.CharField(max_length=50)
    coach = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Matches(models.Model):
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Match in {self.tournament.name} on {self.date}"