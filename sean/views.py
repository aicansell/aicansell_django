from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ItemListSerializer, ItemEmotionSerializer
from .models import Item
from accounts.models import Account
#from organisation.models import Role_Scenario

from rest_framework import status,viewsets
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser 
from accounts.serializers import UserSerializer

import string
from collections import Counter



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

"""
@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def itemlist(request):
    user = UserSerializer(request.user)

    if (user.userorg_roles == Role_Scenario.role_scenario):
        item_list = Item.objects.all().order_by('-id')
        serializer = ItemListSerializer(item_list, many=True)

    # if there is something in items else raise error
        if item_list:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response("No records")        
"""


@api_view(['GET', 'PUT'])
def item_result(request, pk):
    try: 
        item_result = Item.objects.get(pk=pk) 
    except Item.DoesNotExist: 
        return Response({'message': 'The scenario does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        item_data = JSONParser().parse(request) 
        
        
        serializer = ItemEmotionSerializer(item_result)
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

        print(emotions)

        #const myJSON =  JSON.stringify(emotions);

        with open('sean/dump.txt', 'a') as f:
            item1_list = str(item_data)
            f.write(item1_list)
    
        serializer = ItemEmotionSerializer(item_result, data=item_data)
        if serializer.is_valid(): 
            
            item_result.item_answercount = F('item_answercount') + 1
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 