from django.contrib import admin

from SnakeLadderGame.models import SnakeLadderGame, SnakeLadderGameResult, Questions, Options

admin.site.register(SnakeLadderGame)
admin.site.register(SnakeLadderGameResult)
admin.site.register(Questions)
admin.site.register(Options)
