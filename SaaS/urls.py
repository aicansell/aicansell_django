from django.urls import path, include

from rest_framework.routers import DefaultRouter

from SaaS.views import FeatureViewSet, SaaSViewSet

FeatureViewSetRouter = DefaultRouter()
SaaSViewSetRouter = DefaultRouter()

FeatureViewSetRouter.register('', FeatureViewSet, basename='feature')
SaaSViewSetRouter.register('', SaaSViewSet, basename='SaaS-feature')

urlpatterns = [
    path('features/', include(FeatureViewSetRouter.urls)),
    path('user/', include(SaaSViewSetRouter.urls)),
]
