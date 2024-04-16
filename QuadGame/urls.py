from django.urls import path, include

from rest_framework.routers import DefaultRouter

from QuadGame.views import QuadGameListViewSet, QuadGameResultViewSet

QuadGameListViewSetRouter = DefaultRouter()
QuadGameResultViewSetRouter = DefaultRouter()

QuadGameListViewSetRouter.register('', QuadGameListViewSet, basename='quadgame-list')
QuadGameResultViewSetRouter.register('', QuadGameResultViewSet, basename='quadgame-result')

urlpatterns = [
    path('game/', include(QuadGameListViewSetRouter.urls)),
    path('result/', include(QuadGameResultViewSetRouter.urls)),
]
