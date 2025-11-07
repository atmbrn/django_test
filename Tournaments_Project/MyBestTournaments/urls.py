from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_game/", views.add_game, name="add_game"),
    path("add_tournament/", views.add_tournament, name="add_tournament"),
    path("add_team/", views.add_team, name="add_team"),
    path("add_player/", views.add_player, name="add_player"),
    path("add_match/", views.add_match, name="add_match"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register_admin/", views.register_admin, name="register_admin"),
]
