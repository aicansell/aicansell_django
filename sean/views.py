from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ItemListSerializer, ItemEmotionSerializer, SeanSerializer, ItemRecommendSerializer
from .models import Item
from accounts.models import Account
#from organisation.models import Role_Scenario

from rest_framework import status,viewsets, generics, filters
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser 
from accounts.serializers import UserSerializer

import string
from collections import Counter
from django.http import JsonResponse

import speech_recognition as sr
import json
import openai
from decouple import config
import speech_recognition as sr
import pyttsx3

#from rest_framework import viewsets, generics


# Create your views here.

#listing scenarios

@api_view(['GET']) 
def item_list(request):
    
    item_list = Item.objects.all().order_by('-id')
    serializer = ItemListSerializer(item_list, many=True)

    # if there is something in items else raise error
    if item_list:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET']) 
def item_list(request):
    
    item_list = Item.objects.all().order_by('-id')
    serializer = SeanSerializer(item_list, many=True)

    # if there is something in items else raise error
    if item_list:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class ItemList(generics.ListAPIView):
    
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
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
        serializer = ItemListSerializer(items, many=True)
        
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

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def item_result(request, pk):
    try: 
        item_result = Item.objects.get(pk=pk) 
    except Item.DoesNotExist: 
        return Response({'message': 'The scenario does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        item_data = JSONParser().parse(request) 
        
        
        serializer = ItemRecommendSerializer(item_result)
        return Response(serializer.data)
       
        if item_result:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
   
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
        
        
        item1 = Item.objects.get(pk=pk) 
        item1.coming_across_as = my_string
        item1.save()
        #v=item1.coming_across_as
        #print(v)
        

        print(emotions)

        
        #return JsonResponse(emotions, safe=False, status=status.HTTP_200_OK)
        

        #const myJSON =  JSON.stringify(emotions);

        with open('sean/dump.txt', 'a') as f:
            item1_list = str(item_data)
            f.write(item1_list)

       
        serializer = ItemEmotionSerializer(item_result, data=item_data)
        
        if serializer.is_valid(): 
            
            item_result.item_answercount = F('item_answercount') + 1
            serializer.save()
            return JsonResponse({'data': serializer.data, 'coming across as': emotions}, safe=False, status=status.HTTP_200_OK)
            
            #return Response(serializer.data)
            
            
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




