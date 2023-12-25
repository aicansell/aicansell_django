from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_tracking.mixins import LoggingMixin


from icebreaker.models import IceBreaker, IndividualInputScenarios
from icebreaker.serializers import IceBreakerSerializer, IndividualInputScenariosSerializer
from icebreaker.ice_breaker import ice_break_with
from scenarios.models import Scenarios
from scenarios.serializers import ScenariosWordsSerializer

class IceBreakerViewSet(LoggingMixin, ViewSet):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(IceBreaker, pk=pk)
    
    @staticmethod
    def get_queryset(self):
        return IceBreaker.objects.all()
    
    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        # summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(
        #     name=name
        # )
        print(ice_break_with(name=name))
        queryset = self.get_queryset(self)
        serializer = IceBreakerSerializer(queryset, many=True)
        return Response(serializer.data)

class IndividualInputScenariosViewSet(LoggingMixin, ViewSet):
    permission_classes = [IsAuthenticated]
    
    @staticmethod
    def get_object(pk):
        return get_object_or_404(IndividualInputScenarios, pk=pk)
    
    @staticmethod
    def get_queryset():
        return IndividualInputScenarios.objects.all()
    
    def list(self, request, *args, **kwargs):
        serializer = IndividualInputScenariosSerializer(self.get_queryset(), many=True)
        response = {
            'status': 'Success',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = IndividualInputScenariosSerializer(instance)
        response = {
            'status': 'Success',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            'need_help_on': request.data.get('need_help_on'),
            'need_to_talk': request.data.get('need_to_talk'),
            'want_to_say': request.data.get('want_to_say'),
            'come_across_as': request.data.get('come_across_as'),
            'not_come_across_as': request.data.get('not_come_across_as'),
            'created_by': request.user.id
        }
        
        scenarios_data = ScenariosWordsSerializer(Scenarios.objects.all(), many=True).data

        power_word_used = [word['word'] for scenario in scenarios_data for word in scenario['power_words'] if word['word'] in request_data.get('want_to_say')]
        negative_word_used = [word['word'] for scenario in scenarios_data for word in scenario['negative_words'] if word['word'] in request_data.get('want_to_say')]
        
        serializer = IndividualInputScenariosSerializer(data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'Success',
                'data': serializer.data,
                'power_word_used': power_word_used,
                'negative_word_used': negative_word_used
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        response = {
            'status': 'Failure',
            'data': serializer.errors
        }
        
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        
        request_data = {
            'need_help_on': request.data.get('need_help_on', instance.need_help_on),
            'need_to_talk': request.data.get('need_to_talk', instance.need_to_talk),
            'want_to_say': request.data.get('want_to_say', instance.want_to_say),
            'come_across_as': request.data.get('come_across_as', instance.come_across_as),
            'not_come_across_as': request.data.get('not_come_across_as', instance.not_come_across_as),
        }
        
        serializer = IndividualInputScenariosSerializer(instance, data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'Success',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        response = {
            'status': 'Failure',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': 'Success',
            'data': 'Deleted successfully'
        }
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)
