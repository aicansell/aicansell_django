from django.urls import path, include

from rest_framework.routers import DefaultRouter

from assessment.views import Assessment1ViewSet, Assessment2ViewSet, Assessment3ViewSet
from assessment.views import Assessment1ProcessingViewSet, Assessment2ProcessingViewSet, Assessment3ProcessingViewSet

Assessment1ViewSetRouter = DefaultRouter()
Assessment2ViewSetRouter = DefaultRouter()
Assessment3ViewSetRouter = DefaultRouter()
Assessment1ProcessingViewSetRouter = DefaultRouter()
Assessment2ProcessingViewSetRouter = DefaultRouter()
Assessment3ProcessingViewSetRouter = DefaultRouter()

Assessment1ViewSetRouter.register('', Assessment1ViewSet, basename='assessment1')
Assessment2ViewSetRouter.register('', Assessment2ViewSet, basename='assessment2')
Assessment3ViewSetRouter.register('', Assessment3ViewSet, basename='assessment3')
Assessment1ProcessingViewSetRouter.register('', Assessment1ProcessingViewSet, basename='assessment1processing')
Assessment2ProcessingViewSetRouter.register('', Assessment2ProcessingViewSet, basename='assessment2processing')
Assessment3ProcessingViewSetRouter.register('', Assessment3ProcessingViewSet, basename='assessment3processing')

urlpatterns = [
    path('assessment1/', include(Assessment1ViewSetRouter.urls)),
    path('assessment2/', include(Assessment2ViewSetRouter.urls)),
    path('assessment3/', include(Assessment3ViewSetRouter.urls)),
    path('assessment1/processing/', include(Assessment1ProcessingViewSetRouter.urls)),
    path('assessment2/processing/', include(Assessment2ProcessingViewSetRouter.urls)),
    path('assessment3/processing/', include(Assessment3ProcessingViewSetRouter.urls)),
]
