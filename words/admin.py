from django.contrib import admin
from .models import Words, PowerWords1, NegativeWords1, EmotionWords

# Register your models here.

admin.site.register(Words)
admin.site.register(PowerWords1)
admin.site.register(NegativeWords1)
admin.site.register(EmotionWords)