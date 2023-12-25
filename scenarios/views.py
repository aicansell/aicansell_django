from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin

from accounts.models import UserProfile
from scenarios.models import Scenarios
from scenarios.serializers import ScenariosSerializer, ScenariosCreateSerializer

import threading

class ScenariosViewSet(LoggingMixin, ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Scenarios, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Scenarios.objects.all()
    
    def list(self, request):
        serializer = ScenariosSerializer(self.get_queryset(), many=True)
        
        response = {
            'status': "success",
            'data': serializer.data
        }
        
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = ScenariosSerializer(instance)
        response = {
            'status': "success",
            'message': "Retrieved Successfully",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            'item_name': request.data.get('item_name'),
            'power_words': request.data.get('power_words').split(',') if request.data.get('power_words') else [],
            'negative_words': request.data.get('negative_words').split(',') if request.data.get('negative_words') else [],
        }
        
        serializer = ScenariosCreateSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        response = {
            'status': 'success',
            'message': 'Created Successfully',
            'data': serializer.data
        }

        return Response(response, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        
        request_data = {
            'item_name': request.data.get('item_name', instance.item_name),
            'power_words': request.data.get('power_words').split(',') if request.data.get('power_words') else instance.power_words.all(),
            'negative_words': request.data.get('negative_words').split(',') if request.data.get('negative_words') else instance.negative_words.all(),
        }

        serializer = self.get_serializer(instance, data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        response = {
            'status': 'success',
            'message': 'Updated Successfully',
            'data': serializer.data
        }

        return Response(response)
    
    
    def destroy(self, request, pk=None):
        scenario = self.get_object(pk)
        scenario.delete()
        
        response = {
            'status': "success",
            'message': "Deleted Successfully",
        }
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class ScenariosProcessingViewSet(LoggingMixin, ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Scenarios, pk=pk)
    
    def list(self, request, *args, **kwargs):
        def update_user_instance(request, power_words, negative_words):
            print("Updating user instance")
            if request.user.is_authenticated:
                user = UserProfile.objects.get(user=request.user)
                user.user_powerwords = ','.join(filter(None, [user.user_powerwords, ','.join(power_words)]))
                user.user_weakwords = ','.join(filter(None, [user.user_weakwords, ','.join(negative_words)]))
                user.save()
            print("Completed updating user instance")
        
        instance = self.get_object(request.query_params.get('id'))
        
        item_emotions = request.query_params.get('item_emotions')
        own_scenarios = request.query_params.get('own_scenarios')
        
        power_words_list = [str(word.word.word_name) for word in instance.power_words.all()]
        negative_words_list = [str(word.word.word_name) for word in instance.negative_words.all()]

        power_words_used = [word for word in power_words_list if word in item_emotions]
        negative_words_used = [word for word in negative_words_list if word in item_emotions]
                
        processing_thread = threading.Thread(
            target=update_user_instance,
            args=(request, power_words_used, negative_words_used)
        )
        processing_thread.start()
                
        response = {
            'status': 'success',
            'power_words_used': power_words_used,
            'negative_words_used': negative_words_used,
            'score': str(len(power_words_used) - len(negative_words_used)),
            'power_words': power_words_list,
            'negative_words': negative_words_list,
        }
        
        instance.item_emotions = item_emotions+ ", " + instance.item_emotions if instance.item_emotions else ""
        if own_scenarios:
            instance.own_scenarios = own_scenarios+ ", " + instance.own_scenarios if instance.own_scenarios else ""
        instance.save()

        return Response(response, status=status.HTTP_200_OK)
