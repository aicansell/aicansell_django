from django.contrib import admin
from .models import Competency, Sub_Competency, Sub_Competency1, Competency1, Senti, MasterCompetency


# Register your models here.
admin.site.register(Competency)
admin.site.register(Sub_Competency)
admin.site.register(Sub_Competency1)
admin.site.register(Competency1)
admin.site.register(Senti)
admin.site.register(MasterCompetency)