from django.urls import path, include

from rest_framework.routers import DefaultRouter

from sean_scenarios.views import SituationsViewSet, InterestViewSet, TagsViewSet
from sean_scenarios.views import SeanScenariosViewSet, SeanScenarioProcessingViewSet

SituationsRouter = DefaultRouter()
InterestRouter = DefaultRouter()
TagsRouter = DefaultRouter()
SeanScenariosRouter = DefaultRouter()
SeanScenarioProcessingRouter = DefaultRouter()

SituationsRouter.register('', SituationsViewSet, basename='situations')
InterestRouter.register('', InterestViewSet, basename='interests')
TagsRouter.register('', TagsViewSet, basename='tags')
SeanScenariosRouter.register('',SeanScenariosViewSet, basename='sean_scenarios')
SeanScenarioProcessingRouter.register('', SeanScenarioProcessingViewSet, basename='sean_scenario_processing')

urlpatterns = [
    path('sean/', include(SeanScenariosRouter.urls)),
    path('situations/', include(SituationsRouter.urls)),
    path('interests/', include(InterestRouter.urls)),
    path('tags/', include(TagsRouter.urls)),
    path('processing/', include(SeanScenarioProcessingRouter.urls)),
]
