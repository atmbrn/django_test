from django.shortcuts import render, redirect

from .models import Games, Tournaments, Players, Coach, Teams, Matches, SoloMatch, BattleRoyaleMatch, TeamMatch, SoloResult, TeamResult, PlayerStatistics, TeamStatistics, TournamentStatistics
from .forms import GameForm, TournamentForm, PlayerForm, CoachForm, TeamForm, MatchForm, TeamMatchForm, SoloMatchForm, BattleRoyaleMatchForm, SoloResultForm, TeamResultForm, PlayerStatisticsForm, TeamStatisticsForm, TournamentStatisticsForm

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


def add_coach(request):
    if request.method == "POST":
        form = CoachForm(request.POST)
        if form.is_valid():
            coach = Coach(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                experience_years=form.cleaned_data['experience_years'],
                country=form.cleaned_data['country']
            )
            coach.save()
            return redirect('index')
    else:
        form = CoachForm()
    return render(request, 'add_coach.html', {'form': form})


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


def add_team_match(request):
    if request.method == "POST":
        form = TeamMatchForm(request.POST)
        if form.is_valid():
            match = Matches.objects.get(name=form.cleaned_data['match'])
            team_match = TeamMatch(
                match=match,
                date=form.cleaned_data['date']
            )
            team_match.save()
            team_names = form.cleaned_data['teams'].split(',')
            for name in team_names:
                team = Teams.objects.get(name=name.strip())
                team_match.teams.add(team)
            team_match.save()
            return redirect('index')
    else:
        form = TeamMatchForm()
    return render(request, 'add_team_match.html', {'form': form})


def add_solo_match(request):
    if request.method == "POST":
        form = SoloMatchForm(request.POST)
        if form.is_valid():
            match = Tournaments.objects.get(name=form.cleaned_data['match'])
            solo_match = SoloMatch(
                match=match,
                date=form.cleaned_data['date']
            )
            solo_match.save()
            player_names = form.cleaned_data['players'].split(',')
            for name in player_names:
                player = Players.objects.get(name=name.strip())
                solo_match.players.add(player)
            solo_match.save()
            return redirect('index')
    else:
        form = SoloMatchForm()
    return render(request, 'add_solo_match.html', {'form': form})


def add_battle_royale_match(request):
    if request.method == "POST":
        form = BattleRoyaleMatchForm(request.POST)
        if form.is_valid():
            match = Tournaments.objects.get(name=form.cleaned_data['match'])
            br_match = BattleRoyaleMatch(
                match=match,
                date=form.cleaned_data['date']
            )
            br_match.save()
            team_names = form.cleaned_data['teams'].split(',')
            for name in team_names:
                team = Teams.objects.get(name=name.strip())
                br_match.teams.add(team)
            br_match.save()
            return redirect('index')
    else:
        form = BattleRoyaleMatchForm()
    return render(request, 'add_battle_royale_match.html', {'form': form})


def add_solo_result(request):
    if request.method == "POST":
        form = SoloResultForm(request.POST)
        if form.is_valid():
            match = SoloMatch.objects.get(id=form.cleaned_data['match'].id)
            player = Players.objects.get(id=form.cleaned_data['player'].id)
            solo_result = SoloResult(
                match=match,
                players=player,
                score=form.cleaned_data['score']
            )
            solo_result.save()
            return redirect('index')
    else:
        form = SoloResultForm()
    return render(request, 'add_solo_result.html', {'form': form})


def add_team_result(request):
    if request.method == "POST":
        form = TeamResultForm(request.POST)
        if form.is_valid():
            match = BattleRoyaleMatch.objects.get(id=form.cleaned_data['match'].id)
            team = Teams.objects.get(id=form.cleaned_data['team'].id)
            team_result = TeamResult(
                match=match,
                team=team,
                score=form.cleaned_data['score']
            )
            team_result.save()
            return redirect('index')
    else:
        form = TeamResultForm()
    return render(request, 'add_team_result.html', {'form': form})


def add_player_statistics(request):
    if request.method == "POST":
        form = PlayerStatisticsForm(request.POST)
        if form.is_valid():
            player = Players.objects.get(id=form.cleaned_data['player'].id)
            stats = PlayerStatistics(
                player=player,
                matches_played=form.cleaned_data['matches_played'],
                wins=form.cleaned_data['wins'],
                losses=form.cleaned_data['losses'],
                kills=form.cleaned_data['kills'],
                deaths=form.cleaned_data['deaths']
            )
            stats.save()
            return redirect('index')
    else:
        form = PlayerStatisticsForm()
    return render(request, 'add_player_statistics.html', {'form': form})


def add_team_statistics(request):
    if request.method == "POST":
        form = TeamStatisticsForm(request.POST)
        if form.is_valid():
            team = Teams.objects.get(id=form.cleaned_data['team'].id)
            stats = TeamStatistics(
                team=team,
                matches_played=form.cleaned_data['matches_played'],
                wins=form.cleaned_data['wins'],
                losses=form.cleaned_data['losses']
            )
            stats.save()
            return redirect('index')
    else:
        form = TeamStatisticsForm()
    return render(request, 'add_team_statistics.html', {'form': form})


def add_tournament_statistics(request):
    if request.method == "POST":
        form = TournamentStatisticsForm(request.POST)
        if form.is_valid():
            tournament = Tournaments.objects.get(id=form.cleaned_data['tournament'].id)
            stats = TournamentStatistics(
                tournament=tournament,
                total_matches=form.cleaned_data['total_matches'],
                total_teams=form.cleaned_data['total_teams']
            )
            stats.save()
            return redirect('index')
    else:
        form = TournamentStatisticsForm()
    return render(request, 'add_tournament_statistics.html', {'form': form})