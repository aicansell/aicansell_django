from django.contrib import admin

from sean.models import Item, Suggestion, ItemResult

admin.site.register(Item)
admin.site.register(Suggestion)
admin.site.register(ItemResult)
