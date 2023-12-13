from django.urls import path, include

from rest_framework.routers import DefaultRouter

from scenarios.views import ScenariosViewSet

router = DefaultRouter()

router.register("", ScenariosViewSet, basename="scenarios")

urlpatterns = [
    path("", include(router.urls)),
]
