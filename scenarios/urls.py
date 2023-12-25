from django.urls import path, include

from rest_framework.routers import DefaultRouter

from scenarios.views import ScenariosViewSet, ScenariosProcessingViewSet

ScenariosViewSetRouter = DefaultRouter()
ScenariosProcessingViewSetRouter = DefaultRouter()

ScenariosViewSetRouter.register("", ScenariosViewSet, basename="scenarios")
ScenariosProcessingViewSetRouter.register("", ScenariosProcessingViewSet, basename="scenarios_processing")

urlpatterns = [
    path("scenario/", include(ScenariosViewSetRouter.urls)),
    path("scenario_processing/", include(ScenariosProcessingViewSetRouter.urls))
]
