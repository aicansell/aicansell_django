from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orgss.views import OrgViewSet, SubOrgViewSet

OrgViewSetRouter = DefaultRouter()
SubOrgViewSetRouter = DefaultRouter()

OrgViewSetRouter.register('', OrgViewSet, basename='org')
SubOrgViewSetRouter.register('', SubOrgViewSet, basename='suborg')

urlpatterns = [
    path('org/', include(OrgViewSetRouter.urls)),
    path('suborg/', include(SubOrgViewSetRouter.urls)),
]
