from django.contrib import admin
from .models import Item, Suggestion, PowerWords, NegativeWords, EmotionWords

# Register your models here.

admin.site.register(Item)
admin.site.register(Suggestion)
admin.site.register(PowerWords)
admin.site.register(NegativeWords)
admin.site.register(EmotionWords)

