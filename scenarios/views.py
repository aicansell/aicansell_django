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
    
    def create(self, request):
        def update_user_instance(request, power_word, negative_word):
            print("Updating user instance")
            if request.user.is_authenticated:
                user = UserProfile.objects.get(user=request.user)
                user.user_powerwords = ','.join(filter(None, [user.user_powerwords, ','.join(power_words)]))
                user.user_weakwords = ','.join(filter(None, [user.user_weakwords, ','.join(negative_words)]))
                user.save()
            print("Completed updating user instance")
        
        instance = self.get_object(request.data.get('id'))
        
        item_emotions = request.data.get('item_emotions')
        
        power_words = instance.power_words.all()
        negative_words = instance.negative_words.all()
        
        power_words_list = []
        negative_words_list = []
        
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
            'power_words_used': power_words_used,
            'negative_words_used': negative_words_used,
            'score': str(len(power_words_used) - len(negative_words_used)),
            'power_words': power_words_list,
            'negative_words': negative_words_list,
        }

        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = ScenariosSerializer(instance)
        return Response(serializer.data)
    
    
    def destroy(self, request, pk=None):
        scenario = self.get_object(pk)
        scenario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
