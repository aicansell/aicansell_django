from django.urls import path, include
from freemium.views import FreemiumViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('services', FreemiumViewSet, basename='freemium')

urlpatterns = [
    path('', include(router.urls)),
] 