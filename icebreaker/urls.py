from django.urls import path, include

from rest_framework.routers import DefaultRouter

from icebreaker.views import IceBreakerViewSet, IndividualInputScenariosViewSet

router1 = DefaultRouter()
router2 = DefaultRouter()

router1.register('', IceBreakerViewSet, basename='icebreaker')
router2.register('', IndividualInputScenariosViewSet, basename='individualinputscenarios')

urlpatterns = [
    path('process/', include(router1.urls)),
    path('individualinputscenarios/', include(router2.urls)),
]
