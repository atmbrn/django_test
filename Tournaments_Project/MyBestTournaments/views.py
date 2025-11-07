from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.conf import settings
from .forms import GameForm, TournamentForm, PlayerForm, TeamForm, MatchForm, RegisterForm

# Create your views here.


def index(request):
    return render(request=request, template_name="index.html")


def add_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = Games(name=form.cleaned_data['name'])
            game.save()
            return redirect('index')
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})


def add_tournament(request):
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = Tournaments(
                name=form.cleaned_data['name'],
                date=form.cleaned_data['date'],
                location=form.cleaned_data['location'],
                description=form.cleaned_data['description']
            )
            tournament.save()
            return redirect('index')
    else:
        form = TournamentForm()
    return render(request, 'add_tournament.html', {'form': form})


def add_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = Players(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                bio=form.cleaned_data['bio'],
                country=form.cleaned_data['country']
            )
            player.save()
            return redirect('index')
    else:
        form = PlayerForm()
    return render(request, 'add_player.html', {'form': form})


def add_team(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = Teams(
                name=form.cleaned_data['name'],
                country=form.cleaned_data['country'],
                coach=form.cleaned_data['coach']
            )
            team.save()
            player_names = form.cleaned_data['players'].split(',')
            for name in player_names:
                player, created = Players.objects.get_or_create(name=name.strip())
                team.players.add(player)
            team.save()
            return redirect('index')
    else:
        form = TeamForm()
    return render(request, 'add_team.html', {'form': form})


def add_match(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            tournament = Tournaments.objects.get(name=form.cleaned_data['tournament'])
            match = Matches(
                tournament=tournament,
                date=form.cleaned_data['date']
            )
            match.save()
            return redirect('index')
    else:
        form = MatchForm()
    return render(request, 'add_match.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")


def register_admin(request):
    secret = getattr(settings, "ADMIN_SECRET", None)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        code = request.POST.get("secret_code", "")
        if form.is_valid() and secret and code == secret:
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request, "Admin account created.")
            return redirect("login")
        messages.error(request, "Invalid data or secret code.")
    else:
        form = RegisterForm()
    return render(request, "admin_register.html", {"form": form})