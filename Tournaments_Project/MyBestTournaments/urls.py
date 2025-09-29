from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_game/", views.add_game, name="add_game"),
    path("add_tournament/", views.add_tournament, name="add_tournament"),
    path("add_team/", views.add_team, name="add_team"),
    path("add_player/", views.add_player, name="add_player"),
    path("add_coach/", views.add_coach, name="add_coach"),
    path("add_match/", views.add_match, name="add_match"),
    path("add_team_match/", views.add_team_match, name="add_team_match"),
    path("add_battle_royale_match/", views.add_battle_royale_match, name="add_battle_royale_match"),
    path("add_solo_match/", views.add_solo_match, name="add_solo_match"),
    path("add_solo_result/", views.add_solo_result, name="add_solo_result"),
    path("add_team_result/", views.add_team_result, name="add_team_result"),
    path("add_player_statistics/", views.add_player_statistics, name="add_player_statistics"),
    path("add_team_statistics/", views.add_team_statistics, name="add_team_statistics"),
    path("add_tournament_statistics/", views.add_tournament_statistics, name="add_tournament_statistics"),
]
