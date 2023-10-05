from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser 
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin

from django.shortcuts import get_object_or_404
from django.db.models import F
from django.http import JsonResponse

from sean.serializers import ItemListSerializer, ItemEmotionSerializer, ItemRecommendSerializer
from sean.models import Item
from orgss.models import Weightage, Org_Roles
from accounts.models import UserProfile

from collections import Counter
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import speech_recognition as sr
import json
import openai
from decouple import config
import speech_recognition as sr
import pyttsx3


class ItemViewSet(LoggingMixin, ViewSet):
    serializer_class = ItemListSerializer
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

        instance.item_emotion = instance.item_emotion + ',' + emotion_str

        # Tokenize the emotion string into words
        emotion_words = word_tokenize(emotion_str)

        # Remove punctuation and convert to lowercase
        emotion_words = [word.lower() for word in emotion_words if word not in string.punctuation]

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        emotion_words = [word for word in emotion_words if word not in stop_words]

        words = Weightage.objects.filter(org_role=instance.role)

        # Get the associated power_words, negative_words, and emotion_words for each competency
        power_words = words.values_list('competency__sub_competency__power_words', flat=True)
        negative_words = words.values_list('competency__sub_competency__negative_words', flat=True)

        power_words_count = 0
        negative_words_count = 0

        for word in emotion_words:
            if word in power_words:
                instance.user_powerwords = instance.get('user_powerwords', '') + word + ','
                power_words_count += 1
            elif word in negative_words:
                negative_words_count += 1
                instance.user_weakwords = instance.get('user_weakwords', '') + word + ','

        score = power_words_count - negative_words_count

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
            'item_description': instance.item_description,
            'thumbnail': instance.thumbnail,
            'category': instance.category,
            'role': instance.role,
            'item_type': instance.item_type,
            'level': instance.level,
        }

        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)

        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Item was successfully created.'
        }
        return Response(response, status=status.HTTP_201_CREATED)

        
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

