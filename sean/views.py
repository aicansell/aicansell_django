from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ItemListSerializer1, ItemEmotionSerializer, ItemRecommendSerializer,ItemSerializer, ItemLiSerializer
from .models import Item
from accounts.models import Account, UserProfile
#from organisation.models import Role_Scenario

from rest_framework import status,viewsets, generics, filters
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser 
from accounts.serializers import UserSerializer
#from concurrent.futures import ThreadPoolExecutor 

import string
from collections import Counter
from django.http import JsonResponse

import speech_recognition as sr
import json
import openai
from decouple import config
import speech_recognition as sr
import pyttsx3


from rest_framework.viewsets import ViewSet
from rest_framework_tracking.mixins import LoggingMixin

from orgss.models import Weightage, Org_Roles

"""
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize"""


import spacy
nlp = spacy.load('en_core_web_sm')

#from rest_framework import viewsets, generics


# Create your views here.



class ItemViewSet(LoggingMixin, ViewSet):
    serializer_class = ItemListSerializer1
    permission_classes = [IsAuthenticated]


    @staticmethod
    def get_object(pk):
        """Get an Item object by its primary key."""
        return get_object_or_404(Item, id=pk)


    @staticmethod
    def get_queryset():
        """Get all Item objects."""
        return Item.objects.all()


    def list(self, request):
        """
        List items based on user role.


        This view lists items based on the user's role. For admin users, it calculates
        word counts and scenarios attempted counts for each organization role and
        provides a summary of counts for the entire organization.


        Args:
            request: The HTTP request object.


        Returns:
            Response: The HTTP response containing the calculated counts.
        """
        user = self.request.user


        if user.user_role == 'admin':
            org_id = user.role.org
            item_data = Item.objects.filter(role__org=org_id)
            user_data = UserProfile.objects.filter(user__role__org=org_id)
            org_role_names = Org_Roles.objects.filter(org=org_id).values_list('role__name', flat=True)
           
            # Initialize response dictionaries
            response = {
                'org_word_count': sum(len(item.item_emotion.split(' ')) for item in item_data),
                'org_scenarios_attempted': sum(user.scenarios_attempted for user in user_data),
            }
           
            roles_word_count = {}
            roles_scenarios_attempted = {}


            # Calculate word count and scenarios attempted for each organization role
            for org_role in org_role_names:
                users = user_data.filter(user__role__role__name__icontains=org_role)
                roles_word_count[f"{org_id}_{org_role}_word_count"] = sum(len(item.item_emotion.split(' ')) for item in item_data.filter(role__role__name__icontains=org_role))
                roles_scenarios_attempted[f"{org_id}_{org_role}_scenarios_attempted"] = sum(user.scenarios_attempted for user in users)
               
            # Add role-specific counts to the response
            response["roles_word_count"] = roles_word_count
            response["roles_scenarios_attempted"] = roles_scenarios_attempted
           
            # Calculate scenarios attempted for each user
            users_scenarios_attempted = {}
               
            for user in user_data:
                users_scenarios_attempted[f"{user.user.username}_scenarios_attempted"] = user.scenarios_attempted


            # Add user-specific counts to the response
            response["users_scenarios_attempted"] = users_scenarios_attempted
           
            return Response(response, status=status.HTTP_200_OK)
       
        return Response({"message": "You are not authorized to access these details"}, status=status.HTTP_401_UNAUTHORIZED)
       
    def retrieve(self, request, **kwargs):
        """Retrieve a specific item by its primary key."""
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'data': self.serializer_class(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)


    def create(self, request):
        """Create or update an item with emotion analysis."""
        instance = Item.objects.get(id=request.data.get('id'))
        
        emotion_str = request.data.get('item_emotion')

        competency = instance.competencys.all()

        # Initialize an empty list to collect words
        power_word_list = []
        negative_word_list = []

        # Loop through each competency and its sub-competencies
        for competency in competency:
            sub_competencies = competency.sub_competency.all()

            # Loop through each sub-competency and its power words
            for sub_competency in sub_competencies:
                power_words = sub_competency.power_words.all()
                negative_words = sub_competency.negative_words.all()

                # Loop through each power word and its words
                for power_word in power_words:
                    power_word_list.append(power_word.word.word_name)

                for negative_word in negative_words:
                    negative_word_list.append(negative_word.word.word_name)


        instance.item_emotion = instance.item_emotion + ',' + emotion_str


        # Tokenize the emotion string into words
        emotion_words = nlp(emotion_str)
        #emotion_words = word_tokenize(emotion_str)
        for token in emotion_words:
            print(token.text, end = '|')
        for chunks in emotion_words.noun_chunks:
            print(chunks.text)    


        # Remove punctuation and convert to lowercase
        #emotion_words = [word.lower() for word in emotion_words if word not in string.punctuation]


        # Remove stop words
        #stop_words = set(stopwords.words('english'))
        stop_words = spacy.lang.en.stop_words.STOP_WORDS
        emotion_words = [word for word in emotion_words if word.text not in stop_words]
        print(emotion_words)
        

        #print(emotion_words)
        """
        words = Weightage.objects.filter(org_role=instance.role)

        # Get the associated power_words, negative_words, and emotion_words for each competency
        power_words = words.values_list('competency__sub_competency__power_words', flat=True)
        negative_words = words.values_list('competency__sub_competency__negative_words', flat=True)

        #power_words_count = 0
        #negative_words_count = 0"""

        user_power_words = []
        user_weak_words = []
        """
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(process_emotion_word, emotion_words)"""

        for token in emotion_words:
            if token.text in power_words:
                instance.user_powerwords = instance.get('user_powerwords', '') + word + ','
                power_words_count += 1
                user_power_words.append(word)
            elif token.text in negative_words:
                negative_words_count += 1
                instance.user_weakwords = instance.get('user_weakwords', '') + word + ','
                user_weak_words.append(word)

        """
        for chunk in emotion_words.noun_chunks:
            if chunk.text in power_words:
                instance.user_powerwords = instance.get('user_powerwords', '') + word + ','
                power_words_count += 1
                user_power_words.append(word)
            elif chunk.text in negative_words:
                negative_words_count += 1
                instance.user_weakwords = instance.get('user_weakwords', '') + word + ','
                user_weak_words.append(word)  """      


        #score = power_words_count + negative_words_count
        score = len(user_power_words) - len(user_weak_words)


        userprofile_instance = UserProfile.objects.get(user=request.user)
        userprofile_instance.scenarios_attempted += 1
        if userprofile_instance.scenarios_attempted_score:
            userprofile_instance.scenarios_attempted_score += str(score) + ','
        else:
            userprofile_instance.scenarios_attempted_score = str(score) + ','
        userprofile_instance.save()


        instance.save()
        
        data = {
            'id': instance.id,
            'item_name': instance.item_name,
            #'item_description': instance.item_description,
            #'thumbnail': instance.thumbnail,
            #'category': instance.category,
            #'role': instance.role_id,
            #'item_type': instance.item_type,
            #'level': instance.level,
            #'competencys': instance.competencys
            'coming_across_as': instance.coming_across_as
        }
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
       
        
        data = serialized_data.data

        response_data = {
            'id': data.get('id'),
            'item_name': data.get('item_name'),
            #'item_description': data.get('item_description'),
            #'thumbnail': data.get('thumbnail'),
            #'category': data.get('category'),
            #'role': data.get('role_id'),
            #'item_type': data.get('item_type'),
            #'level': data.get('level'),
            'coming_across_as': data.get('coming_across_as'),
            'compentency_score': score,
            'powerword_detected': user_power_words,
            'weekword_detected': user_weak_words,
            'power_word_list': power_word_list,
            'negative_word_list': negative_word_list,
            #'competencys': data.get('competencys')
        }
        #serialized_data = self.serializer_class(data=data)
        #serialized_data.is_valid(raise_exception=True)

        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        response = {
            'status': 'Success',
            #'data': serialized_data.data,
            'data': response_data,
            'message': 'Item was successfully created.'
        }
        return Response(response, status=status.HTTP_201_CREATED)


class ItemHandleViewSet(LoggingMixin, ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Item, id=pk)

    @staticmethod
    def get_queryset():
        return Item.objects.all()

    def list(self, request):
        data = Item.objects.filter(role=self.request.user.role).order_by('-id')

        serializer_data = self.serializer_class(data, many=True).data
        response = {
            'status': 'Success',
            'data': serializer_data,
        }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, **kwargs):
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'data': self.serializer_class(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request):
        request_data = self.request.data
        data = {
            'item_name': request_data.get('item_name'),
            #'item_description': request_data.get('item_description'),
            #er': request_data.get('item_answer'),
            'item_emotion': request_data.get('item_emotion'),
            'item_answercount': request_data.get('item_answercount'),
            'category': request_data.get('category'),
            'thumbnail': request_data.get('thumbnail'),
            'item_gender': request_data.get('item_gender'),
            'item_type': request_data.get('item_type'),
            'role': request_data.get('role'),
            'coming_across_as': request_data.get('coming_across_as'),
            'competencys': request_data.get('competencys'),
            'level': request_data.get('level'),
            #'positive_traits': request_data.get('positive_traits'),
            #'negative_traits': request_data.get('negative_traits'),
            'user_powerwords': request_data.get('user_powerwords'),
            'user_weakwords': request_data.get('user_weakwords'),
            #'expert': request_data.get('expert'),
        }

        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Item was successfully created.'
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        request_data = self.request.data

        data = {
            'item_name': request_data.get('item_name', instance.item_name),
            #'item_description': request_data.get('item_description', instance.item_description),
            #'item_answer': request_data.get('item_answer', instance.item_answer),
            'item_emotion': request_data.get('item_emotion', instance.item_emotion),
            'item_answercount': request_data.get('item_answercount', instance.item_answercount),
            'category': request_data.get('category', instance.category),
            'thumbnail': request_data.get('thumbnail', instance.thumbnail),
            'item_gender': request_data.get('item_gender', instance.item_gender),
            'item_type': request_data.get('item_type', instance.item_type),
            'role': request_data.get('role', instance.role_id),
            'coming_across_as': request_data.get('coming_across_as', instance.coming_across_as),
            'competencys': request_data.get('competencys', instance.competencys),
            'level': request_data.get('level', instance.level),
            #'positive_traits': request_data.get('positive_traits', instance.positive_traits),
            #'negative_traits': request_data.get('negative_traits', instance.negative_traits),
            'user_powerwords': request_data.get('user_powerwords', instance.user_powerwords),
            'user_weakwords': request_data.get('user_weakwords', instance.user_weakwords),
            #'expert': request_data.get('expert', instance.expert),
        }

        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Item was successfully updated.'
        }
        return Response(response, status=status.HTTP_200_OK)


    def destroy(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        instance.delete()

        response = {
            'data': '',
            'message': "Successfully deleted Item"
        }

        return Response(response, status=status.HTTP_204_NO_CONTENT)
       



#listing scenarios
"""
@api_view(['GET']) 
def item_list(request):
    
    item_list = Item.objects.all().order_by('-id')
    serializer = ItemListSerializer(item_list, many=True)

    # if there is something in items else raise error
    if item_list:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
"""

class ItemList(generics.ListAPIView):
    
    queryset = Item.objects.all()
    serializer_class = ItemLiSerializer
    permission_classes = [IsAuthenticated]
   

    def list(self,request):
        
        user = request.user
        
        #getting user's role id
        u2 = user.role_id
        
        """
        u2 = Account.objects.values_list('role')
        print(u2)
        """

        items = Item.objects.filter(role = u2).order_by('-id')
        serializer = ItemLiSerializer(items, many=True)
        
        if items:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
"""
# Initialize the recognizer
r = sr.Recognizer()

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     

while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")

"""
#whisper
"""
import openai
import wave
import pyaudio

openai.api_key =

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []


try:
   while True:
       data = stream.read(1024)
       frames.append(data)
except KeyboardInterrupt:
   pass


stream.stop_stream()
stream.close()
audio.terminate()


sound_file = wave.open("myrecording.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b"".join(frames))
sound_file.close()


audio_file = open("myrecording.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)


print(transcript['text'])

"""

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
            return JsonResponse({'data': serializer.data, 'coming across as': emotions}, safe=False, status=status.HTTP_200_OK)
            
            #return Response(serializer.data)
            
            
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


