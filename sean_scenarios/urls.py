from django.urls import path, include

from rest_framework.routers import DefaultRouter

from sean_scenarios.views import SituationsViewSet, InterestViewSet, TagsViewSet, SeanScenariosViewSet

SituationsRouter = DefaultRouter()
InterestRouter = DefaultRouter()
TagsRouter = DefaultRouter()
SeanScenariosRouter = DefaultRouter()

SituationsRouter.register('', SituationsViewSet, basename='situations')
InterestRouter.register('', InterestViewSet, basename='interests')
TagsRouter.register('', TagsViewSet, basename='tags')
SeanScenariosRouter.register('',SeanScenariosViewSet, basename='sean_scenarios')

urlpatterns = [
    path('situations/', include(SituationsRouter.urls)),
    path('interests/', include(InterestRouter.urls)),
    path('tags/', include(TagsRouter.urls)),
    path('', include(SeanScenariosRouter.urls)),
]
