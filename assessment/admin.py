from django.contrib import admin

from assessment.models import Style, Situation
from assessment.models import Assessment1, Assessment2, Assessment3

admin.site.register(Style)
admin.site.register(Situation)
admin.site.register(Assessment1)
admin.site.register(Assessment2)
admin.site.register(Assessment3)
