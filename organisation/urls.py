from django.urls import path, include
from rest_framework.routers import DefaultRouter

from organisation.views import OrgViewSet

router = DefaultRouter()
router.register('org', OrgViewSet, basename='org')

urlpatterns = [
    path('', include(router.urls)),
]