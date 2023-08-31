from django.contrib import admin
from .models import Option, YourAnswer, Feedback, Quiz, Quiz_Roles


# Register your models here.


admin.site.register(Option)
admin.site.register(YourAnswer)
admin.site.register(Feedback)
admin.site.register(Quiz)
admin.site.register(Quiz_Roles)
