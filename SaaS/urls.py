from django.urls import path, include

from rest_framework.routers import DefaultRouter

from SaaS.views import FeatureViewSet, SaaSViewSet, LevelAccessCheck

FeatureViewSetRouter = DefaultRouter()
SaaSViewSetRouter = DefaultRouter()
LevelAccessCheckRouter = DefaultRouter()

FeatureViewSetRouter.register('', FeatureViewSet, basename='feature')
SaaSViewSetRouter.register('', SaaSViewSet, basename='SaaS-feature')
LevelAccessCheckRouter.register('', LevelAccessCheck, basename='Level-Access-Check')

urlpatterns = [
    path('features/', include(FeatureViewSetRouter.urls)),
    path('user/', include(SaaSViewSetRouter.urls)),
    path('levelcheck/', include(LevelAccessCheckRouter.urls)),
]
