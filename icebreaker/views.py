from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_tracking.mixins import LoggingMixin


from icebreaker.models import IceBreaker, IndividualInputScenarios, IceBreakerData
from icebreaker.serializers import IceBreakerSerializer, IndividualInputScenariosSerializer
from icebreaker.ice_breaker import ice_break_with
from scenarios.models import Scenarios
from scenarios.serializers import ScenariosWordsSerializer
from accounts.throttling import UserBasedAnonRateThrottle

class IceBreakerViewSet(LoggingMixin, ViewSet):
    throttle_classes = [UserBasedAnonRateThrottle]
    
    @staticmethod
    def get_object(pk):
        return get_object_or_404(IceBreaker, pk=pk)
    
    @staticmethod
    def get_queryset(self):
        return IceBreaker.objects.all()
    
    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        try:
            instance = IceBreakerData.objects.get(username=name)
            
            response = {
                'status': 'Success',
                'message': 'Analysis successfully',
                'data': instance.process_data
            }
            
            return Response(response, status=status.HTTP_200_OK)
        except IceBreakerData.DoesNotExist:
            try:
                summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(
                    name=name
                )
                response = {
                    'status': 'Success',
                    'message': 'Analysis successfully',
                    'data': {
                        'summary_and_facts': summary_and_facts,
                        'interests': interests,
                        'ice_breakers': ice_breakers,
                        'profile_pic_url': profile_pic_url
                    }
                }
                
                obj = IceBreakerData.objects.create(username=name, process_data=str(response['data']))
                obj.save()
                
                return Response(response, status=status.HTTP_200_OK)
            except:
                response = {
                    'status': 'Failure',
                    'message': 'Failed to analyse, Try Again',
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
    
    def create(self, request):
        request_data = {
            'going_for': request.data.get('going_for'),
            'with_who': request.data.get('with_who'),
            'help_on': request.data.get('help_on'),
            'come_across_as': request.data.get('come_across_as'),
            'not_come_across_as': request.data.get('not_come_across_as'),
        }
        
        if self.request.user.is_authenticated:
            request_data['created_by'] = request.user.id
        
        serializer = IceBreakerSerializer(data=request_data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                'status': 'Success',
                'message': 'Created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': 'Failure',
            'message': 'Failed to create',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        
        request_data = {
            'going_for': request.data.get('going_for', instance.going_for),
            'with_who': request.data.get('with_who', instance.with_who),
            'help_on': request.data.get('help_on', instance.help_on),
            'come_across_as': request.data.get('come_across_as', instance.come_across_as),
            'not_come_across_as': request.data.get('not_come_across_as', instance.not_come_across_as),
        }
        
        serializer = IceBreakerSerializer(instance, data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'Success',
                'message': 'Updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        response = {
            'status': 'Failure',
            'message': 'Failed to update',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': 'Success',
            'message': 'Deleted successfully'
        }
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)

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
