from django.urls import path, include

from rest_framework.routers import DefaultRouter

from assign.views import SeriesAssignUserViewSet, ProgressCheckViewSet
from assign.views import AssessmentProgressViewSet, ItemProgressViewSet

SeriesAssignUserViewSetRouter = DefaultRouter()
AssessmentProgressViewSetRouter = DefaultRouter()
ItemProgressViewSetRouter = DefaultRouter()
ProgressCheckViewSetRouter = DefaultRouter()

SeriesAssignUserViewSetRouter.register("", SeriesAssignUserViewSet, basename="series-assign-user")
AssessmentProgressViewSetRouter.register("", AssessmentProgressViewSet, basename="assessment-progress")
ItemProgressViewSetRouter.register("", ItemProgressViewSet, basename="item-progress")
ProgressCheckViewSetRouter.register("", ProgressCheckViewSet, basename="progress-check")

urlpatterns = [
    path("series/", include(SeriesAssignUserViewSetRouter.urls)),
    path("assessmentprogress/", include(AssessmentProgressViewSetRouter.urls)),
    path("itemprogress/", include(ItemProgressViewSetRouter.urls)),
    path("progresscheck/", include(ProgressCheckViewSetRouter.urls)),
]
