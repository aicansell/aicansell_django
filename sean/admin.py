from django.contrib import admin
from .models import Item, Suggestion, Traits, Collection

# Register your models here.


admin.site.register(Item)
admin.site.register(Suggestion)
admin.site.register(Traits)
admin.site.register(Collection)
