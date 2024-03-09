from django.urls import path, include

from rest_framework.routers import DefaultRouter

from assign.views import SeriesAssignUserViewSet

SeriesAssignUserViewSetRouter = DefaultRouter()

SeriesAssignUserViewSetRouter.register("", SeriesAssignUserViewSet, basename="series-assign-user")

urlpatterns = [
    path("series/", include(SeriesAssignUserViewSetRouter.urls))
]
