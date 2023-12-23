from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin


from icebreaker.models import IceBreaker, IndividualInputScenarios
from icebreaker.serializers import IceBreakerSerializer, IndividualInputScenariosSerializer
from icebreaker.ice_breaker import ice_break_with

class IceBreakerViewSet(LoggingMixin, ViewSet):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(IceBreaker, pk=pk)
    
    @staticmethod
    def get_queryset(self):
        return IceBreaker.objects.all()
    
    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(
            name=name
        )
        print(summary_and_facts, interests, ice_breakers, profile_pic_url)
        queryset = self.get_queryset(self)
        serializer = IceBreakerSerializer(queryset, many=True)
        return Response(serializer.data)


class IndividualInputScenariosViewSet(LoggingMixin, ViewSet):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(IndividualInputScenarios, pk=pk)
    
    @staticmethod
    def get_queryset():
        return IndividualInputScenarios.objects.all()
    
    def list(self, request, *args, **kwargs):
        serializer = IndividualInputScenariosSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
