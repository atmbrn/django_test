from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User     

from .models import models, Games, Tournaments, Players, Teams, Matches


class GameForm(forms.Form):
    name = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    release_date = forms.DateField()


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


class TeamForm(forms.Form):
    name = forms.CharField(max_length=100)
    players = forms.CharField(widget=forms.Textarea, help_text="Enter player names separated by commas")
    country = forms.CharField(max_length=50)


class MatchForm(forms.Form):
    tournament = forms.CharField(max_length=100)
    date = forms.DateTimeField()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")