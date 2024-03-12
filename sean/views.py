from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status,viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ViewSet
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.viewsets import ViewSet
from rest_framework_tracking.mixins import LoggingMixin

from .serializers import ItemListSerializer1, ItemEmotionSerializer, ItemRecommendSerializer,ItemSerializer, ItemLiSerializer, ItemUserSerializer
from .models import Item
from accounts.models import Account, UserProfile
from orgss.models import Weightage

import string
from collections import Counter
import speech_recognition as sr
import json
from decouple import config
import speech_recognition as sr
import spacy
import threading
nlp = spacy.load('en_core_web_sm')


class ItemViewSet(LoggingMixin, ViewSet):
    serializer_class = ItemListSerializer1
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Item, id=pk)

    @staticmethod
    def get_queryset():
        return Item.objects.all()

    def list(self, request):
        user = self.request.user

        if user.user_role == 'admin' or user.user_role == 'superadmin':
            org_id = user.role.org
            item_data = Item.objects.filter(role__org=org_id)
            user_data = UserProfile.objects.filter(user__role__org=org_id)

            response = {
                'org_word_count': sum(len(item.item_emotion.split(' ')) for item in item_data),
                'org_scenarios_attempted': sum(user.scenarios_attempted for user in user_data),
            }
           
            roles_word_count = {}
            roles_scenarios_attempted = {}

            for org_role in org_role_names:
                users = user_data.filter(user__role__org_role_name__icontains=org_role)
                roles_word_count[f"{org_id}_{org_role}_word_count"] = sum(len(item.item_emotion.split(' ')) for item in item_data.filter(role__org_role_name__icontains=org_role))
                roles_scenarios_attempted[f"{org_id}_{org_role}_scenarios_attempted"] = sum(user.scenarios_attempted for user in users)
               
            response["roles_word_count"] = roles_word_count
            response["roles_scenarios_attempted"] = roles_scenarios_attempted
           
            users_scenarios_attempted = {}
               
            for user in user_data:
                users_scenarios_attempted[f"{user.user.username}_scenarios_attempted"] = user.scenarios_attempted

            response["users_scenarios_attempted"] = users_scenarios_attempted
           
            return Response(response, status=status.HTTP_200_OK)
       
        return Response({"message": "You are not authorized to access these details"}, status=status.HTTP_401_UNAUTHORIZED)
       
    def retrieve(self, request, **kwargs):
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'message': 'Retrieved Successfully',
            'data': self.serializer_class(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)

class ItemHandleViewSet(LoggingMixin, ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemUserSerializer

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Item, id=pk)

    @staticmethod
    def get_queryset():
        return Item.objects.all()

    @method_decorator(cache_page(60 * 15))
    def list(self, request):
        data = Item.objects.filter(role=self.request.user.role).order_by('-id')

        serializer_data = self.serializer_class(data, many=True).data
        response = {
            'status': 'Success',
            'message': 'Retrieved Successfully',
            'data': serializer_data,
        }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, **kwargs):
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'message': 'Retrieved Successfully',
            'data': self.serializer_class(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)
       
class ItemProcessingViewSet(LoggingMixin, ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemListSerializer1
    
    def list(self, request):
        def process_user_data(userprofile_instance, user_power_words, user_weak_words, score, competencys, emotion_words):
            print("\n\nStarting Thread: UserProfile")
            userprofile_instance.scenarios_attempted += 1
            userprofile_instance.user_powerwords = (userprofile_instance.user_powerwords or '') + "," + ", ".join(user_power_words)
            userprofile_instance.user_weakwords = (userprofile_instance.user_weakwords or '') + "," + ", ".join(user_weak_words)
            userprofile_instance.user_powerwords = userprofile_instance.user_powerwords.strip(',')
            userprofile_instance.user_weakwords = userprofile_instance.user_weakwords.strip(',')
            if userprofile_instance.scenarios_attempted_score:
                userprofile_instance.scenarios_attempted_score += str(score) + ','
            else:
                userprofile_instance.scenarios_attempted_score = str(score) + ','
            print("\n\nCompleted Thread: UserProfile")
            print("\n\nStarting Thread: Update Competency")
            try:
                competency_score = json.loads(userprofile_instance.competency_score)
            except:
                competency_score = {}

            for competency in competencys:
                sub_competencies = competency.sub_competency.all()
                power_word_list = []
                negative_word_list = []

                for sub_competency in sub_competencies:
                    power_words = sub_competency.power_words.all()
                    negative_words = sub_competency.negative_words.all()

                    for power_word in power_words:
                        power_word_list.append(power_word.word.word_name.lower())

                    for negative_word in negative_words:
                        negative_word_list.append(negative_word.word.word_name.lower())

                power_word_count = 0
                negative_word_count = 0
                
                power_word_count = sum(1 for word in power_word_list if word in emotion_words)
                negative_word_count = sum(1 for word in negative_word_list if word in emotion_words)

                
                competency_name = str(competency.competency_name)
                        
                if competency_name in competency_score:
                    competency_score[competency_name] += ',' + str(power_word_count - negative_word_count)
                    competency_score[competency_name] = competency_score[competency_name]
                else:
                    competency_score[competency_name] = str(power_word_count - negative_word_count)

            userprofile_instance.competency_score = json.dumps(competency_score)
            userprofile_instance.save()
            print("\n\nCompleted Thread: Update Competency")
        try:
            instance = Item.objects.get(id=request.query_params.get('id'))
        except Item.DoesNotExist:
            response = {
                'status': 'Failed',
                'message': 'Scenario does not exist'
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
        userprofile_instance = UserProfile.objects.get(user=request.user)
        
        emotion_str = request.query_params.get('item_emotion').lower()
        
        competencys = instance.competencys.all().prefetch_related(
            'sub_competency__power_words__word',
            'sub_competency__negative_words__word'
        )
        
        power_word_list = []
        negative_word_list = []
        
        for competency in competencys:
            sub_competencies = competency.sub_competency.all()
            for sub_competency in sub_competencies:
                power_words = sub_competency.power_words.all()
                negative_words = sub_competency.negative_words.all()

                for power_word in power_words:
                    power_word_list.append(power_word.word.word_name.lower())

                for negative_word in negative_words:
                    negative_word_list.append(negative_word.word.word_name.lower())
        
        instance.item_emotion = instance.item_emotion + ',' + emotion_str
        
        user_power_words = []
        user_weak_words = []
        
        for words in power_word_list:
            if words in emotion_str:
                user_power_words.append(words)
        for words in negative_word_list:
            if words in emotion_str:
                user_weak_words.append(words)
        
        score = len(user_power_words) - len(user_weak_words)

        instance.item_answercount += 1
        
        processing_thread = threading.Thread(
            target=process_user_data,
            args=(userprofile_instance, user_power_words, user_weak_words, score, competencys, emotion_str)
        )
        processing_thread.start()
        
        data = {
            'id': instance.id,
            'item_name': instance.item_name,
            'coming_across_as': instance.coming_across_as
        }
        instance.save()
        
        response_data = {
            'id': data.get('id'),
            'item_name': data.get('item_name'),
            'coming_across_as': data.get('coming_across_as'),
            'compentency_score': score,
            'powerword_detected': user_power_words,
            'weekword_detected': user_weak_words,
            'power_word_list': power_word_list,
            'negative_word_list': negative_word_list,
        }
        
        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = {
            'status': 'Success',
            'message': 'Item was successfully created.',
            'data': response_data,
        }
        return Response(response, status=status.HTTP_200_OK)
        
class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemLiSerializer
    permission_classes = [IsAuthenticated]

    def list(self,request):
        user = request.user
        u2 = user.role_id

        items = Item.objects.filter(role = u2).order_by('-id')
        serializer = ItemLiSerializer(items, many=True)
        
        if items:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ItemAnalysticsViewSet(LoggingMixin, ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        user_instance = UserProfile.objects.get(user=request.user)
        
        user_details = {
            'power_words_used': user_instance.user_powerwords,
            'week_words_used': user_instance.user_weakwords,
            'scenarios_attempted': user_instance.scenarios_attempted,
            'scenarios_attempted_score': user_instance.scenarios_attempted_score,
            'competency_score': json.loads(user_instance.competency_score) if user_instance.competency_score else {},
        }
        
        response = {
            'status': 'Success',
            'message': 'Retrieved Successfully',
            'data': user_details,
        }
        
        return Response(response, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def item_result(request, pk):
    try: 
        item_result = Item.objects.get(pk=pk) 
    except Item.DoesNotExist: 
        return Response({'message': 'The scenario does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    
    if request.method == 'PUT': 
        item_data = JSONParser().parse(request) 
        
        #itemli = Item.objects.get(id=pk)
        item = Item.objects.values_list('item_answer').get(id=pk)
        
        with open('sean/read.txt', 'w') as f:
            item_list = str(item_data)
            f.write(item_list)
        
        text = open('sean/read.txt').read() 
        lower_case = text.lower()   
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
        
        tokenized_words = cleaned_text.split()
    

        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "or", "because", "as",
              "of", "at", "by", "for", "with", "about", "against", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "here", "there", "any", "both", "each",
              "few", "other", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "s", "t", "can", "will", "just", "don"]

        final_words = []
        for word in tokenized_words:
            if word not in stop_words:
                final_words.append(word)

        emotion_c1 = []
        with open('sean/emotions.txt', 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')
                
                if word in final_words:
                    emotion_c1.append(emotion)


        emotion_count = Counter(emotion_c1)
        emotions = str(emotion_count)[9: -2]
        unique_list = list(set(emotion_c1))
        my_string = ", ".join(unique_list)
        

        print(emotions)

        
        #return JsonResponse(emotions, safe=False, status=status.HTTP_200_OK)
        

        #const myJSON =  JSON.stringify(emotions);

        with open('sean/dump.txt', 'a') as f:
            item1_list = str(item_data)
            f.write(item1_list)

       
        serializer = ItemEmotionSerializer(item_result, data=item_data)
        
        if serializer.is_valid(): 
            
            item_result.item_answercount = F('item_answercount') + 1
            item_result.coming_across_as = my_string
            serializer.save()
            return JsonResponse({'data': serializer.data, 'coming_across_as': emotions}, safe=False, status=status.HTTP_200_OK)
            
            #return Response(serializer.data)
            
            
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def item_rec(request, pk):
    try: 
        item_result = Item.objects.get(pk=pk) 
    except Item.DoesNotExist: 
        return Response({'message': 'The scenario does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        #item_data = JSONParser().parse(request) 
        
        
        serializer = ItemRecommendSerializer(item_result)
        #serializer = ItemRecoSerializer(item_result)
        return Response(serializer.data)
       
        if item_result:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
