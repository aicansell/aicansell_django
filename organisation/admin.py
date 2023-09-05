from django.contrib import admin
from .models import Org, Org_Roles

# Register your models here.
admin.site.register(Org)

admin.site.register(Org_Roles)

#admin.site.register(Role_Scenario)
