from django.urls import path, include

from rest_framework.routers import DefaultRouter

from series.views import SeriesViewSet, SeasonsViewSet

SeriesViewSetRouter = DefaultRouter()
SeasonsViewSetRouter = DefaultRouter()

SeriesViewSetRouter.register("", SeriesViewSet, basename="SeriesViewSet")
SeasonsViewSetRouter.register("", SeasonsViewSet, basename="SeasonsViewSet")

urlpatterns = [
    path("series/", include(SeriesViewSetRouter.urls)),
    path("seasons/", include(SeasonsViewSetRouter.urls)),
]
