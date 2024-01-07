from django.contrib import admin

from sean_scenarios.models import SeanScenarios, SeanScenariosSituations, SeanScenariosInterests, SeanScenariosTags
from sean_scenarios.models import Interest, Situations, Tags

admin.site.register(Interest)
admin.site.register(Situations)
admin.site.register(Tags)
admin.site.register(SeanScenarios)
admin.site.register(SeanScenariosSituations)
admin.site.register(SeanScenariosInterests)
admin.site.register(SeanScenariosTags)
