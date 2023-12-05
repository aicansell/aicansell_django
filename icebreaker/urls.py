from django.urls import path, include

from rest_framework.routers import DefaultRouter

from icebreaker.views import IceBreakerViewSet

router = DefaultRouter()

router.register('process', IceBreakerViewSet, basename='icebreaker')

urlpatterns = [
    path('', include(router.urls)),
]
