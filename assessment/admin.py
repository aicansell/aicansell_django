from django.contrib import admin

from assessment.models import Question, Option, AssessmentType
from assessment.models import Assessment, AssessmentResult

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(AssessmentType)
admin.site.register(Assessment)
admin.site.register(AssessmentResult)
