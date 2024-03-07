from django.contrib import admin

from series.models import Series, Seasons, AssessmentSeason, LearningCourseSeason, ItemSeason

admin.site.register(Series)
admin.site.register(Seasons)
admin.site.register(AssessmentSeason)
admin.site.register(LearningCourseSeason)
admin.site.register(ItemSeason)
