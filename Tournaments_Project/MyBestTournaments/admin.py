from django.contrib import admin

from .models import Games, Tournaments, Players, Coach, Teams, Matches, SoloMatch, BattleRoyaleMatch, TeamMatch, SoloResult, TeamResult, PlayerStatistics, TeamStatistics, TournamentStatistics


# Register your models here.


admin.site.register([Games, Tournaments, Players, Coach, Teams, Matches, SoloMatch, BattleRoyaleMatch, TeamMatch, SoloResult, TeamResult, PlayerStatistics, TeamStatistics, TournamentStatistics])