from django import forms

from .models import models, Tournaments, Players, Teams, SoloMatch, BattleRoyaleMatch, Teams, SoloResult, TeamResult, PlayerStatistics, TeamStatistics, TournamentStatistics


class GameForm(forms.Form):
    name = forms.CharField(max_length=100)


class TournamentForm(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateField()
    location = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class PlayerForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    bio = forms.CharField(widget=forms.Textarea)
    country = forms.CharField(max_length=50)


class CoachForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    experience_years = forms.IntegerField()
    country = forms.CharField(max_length=50)


class TeamForm(forms.Form):
    name = forms.CharField(max_length=100)
    players = forms.CharField(widget=forms.Textarea, help_text="Enter player names separated by commas")
    country = forms.CharField(max_length=50)
    coach = forms.CharField(max_length=100)


class MatchForm(forms.Form):
    tournament = forms.CharField(max_length=100)
    date = forms.DateTimeField()


class TeamMatchForm(forms.Form):
    match = forms.CharField(max_length=100)
    teams = forms.CharField(max_length=100)
    date = forms.DateTimeField()


class SoloMatchForm(forms.Form):
    match = forms.CharField(max_length=100)
    players = forms.CharField(max_length=100)
    date = forms.DateTimeField()


class BattleRoyaleMatchForm(forms.Form):
    match = forms.CharField(max_length=100)
    teams = forms.CharField(widget=forms.Textarea, help_text="Enter team names separated by commas")
    date = forms.DateTimeField()


class SoloResultForm(forms.Form):
    match = forms.ModelChoiceField(queryset=SoloMatch.objects.all())
    players = forms.ModelChoiceField(queryset=Players.objects.all())
    score = forms.IntegerField()


class TeamResultForm(forms.Form):
    match = forms.ModelChoiceField(queryset=BattleRoyaleMatch.objects.all())
    teams = forms.ModelChoiceField(queryset=Teams.objects.all())
    score = forms.IntegerField()


class PlayerStatisticsForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Players.objects.all())
    matches_played = forms.IntegerField()
    wins = forms.IntegerField()
    losses = forms.IntegerField()
    kills = forms.IntegerField()
    deaths = forms.IntegerField()


class TeamStatisticsForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Teams.objects.all())
    matches_played = forms.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()


class TournamentStatisticsForm(forms.Form):
    tournament = forms.ModelChoiceField(queryset=Tournaments.objects.all())
    total_matches = forms.IntegerField()
    total_teams = forms.IntegerField()