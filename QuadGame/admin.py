from django.contrib import admin

from QuadGame.models import QuadGame, Quadrant, QuadGameResult
from QuadGame.models import Statements, Questions

admin.site.register(QuadGame)
admin.site.register(Quadrant)
admin.site.register(Statements)
admin.site.register(Questions)
admin.site.register(QuadGameResult)
