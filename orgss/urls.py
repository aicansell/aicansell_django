from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orgss.views import OrgViewSet, OrgRolesViewSet, WeightageViewSet

router = DefaultRouter()
router.register('org', OrgViewSet, basename='org')
router.register('org_roles', OrgRolesViewSet, basename='org_roles')
router.register('weightage', WeightageViewSet, basename='weightage')


urlpatterns = [
    path('', include(router.urls)),
]