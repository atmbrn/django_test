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


class Coach(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    experience_years = models.IntegerField()
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


class TeamMatch(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Teams)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Team match in {self.match.tournament.name} on {self.match.date}"


class SoloMatch(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    players = models.ManyToManyField(Players)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Solo match in {self.match.tournament.name} with {self.players.count()} players"


class BattleRoyaleMatch(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Teams)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Battle Royale in {self.match.tournament.name} with {self.teams.count()} teams"


class SoloResult(models.Model):
    match = models.ForeignKey(SoloMatch, on_delete=models.CASCADE)
    players = models.ForeignKey(Players, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.players.name} scored {self.score} in {self.match}"


class TeamResult(models.Model):
    match = models.ForeignKey(BattleRoyaleMatch, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} scored {self.score} in {self.match}"


class PlayerStatistics(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()

    def __str__(self):
        return f"Stats for {self.player.name}"


class TeamStatistics(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()

    def __str__(self):
        return f"Stats for {self.team.name}"


class TournamentStatistics(models.Model):
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    total_matches = models.IntegerField()
    total_teams = models.IntegerField()

    def __str__(self):
        return f"Stats for {self.tournament.name}"