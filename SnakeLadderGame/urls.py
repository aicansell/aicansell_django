from django.urls import path, include

from SnakeLadderGame.views import SnakeLadderGameViewSet, SnakeLadderGameResultViewSet
from SnakeLadderGame.views import QuestionsViewSet, OptionsViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('game', SnakeLadderGameViewSet, basename='snakeladdergame')
router.register('result',SnakeLadderGameResultViewSet, basename='snakeladdergameresult')
router.register('questions', QuestionsViewSet, basename='snakeladdergamequestions')
router.register('options', OptionsViewSet, basename='snakeladdergameoptions')

urlpatterns = [
    path('', include(router.urls)),
]
