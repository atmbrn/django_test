from django.contrib import admin

from .models import Games, Tournaments, Players, Teams, Matches

# Register your models here.


admin.site.register([Games, Tournaments, Players, Teams, Matches])