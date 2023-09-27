from django.contrib import admin
from .models import Org, Org_Roles, Weightage

# Register your models here.
admin.site.register(Org)

admin.site.register(Org_Roles)

admin.site.register(Weightage)

#admin.site.register(Role_Scenario)