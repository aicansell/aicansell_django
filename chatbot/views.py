from django.shortcuts import render
from openai import ChatCompletion
import openai
from decouple import config

from rest_framework.decorators import api_view

from django.http import JsonResponse
from rest_framework.parsers import JSONParser 
import json
from rest_framework import status

openai.api_key = config('api_key')


   
@api_view(['POST'])
def chatresponse(request):
    """if request.method == 'GET': 
        item_data = JSONParser().parse(request)
        print(item_data)
    """    
    
    if request.method == 'POST': 
        item_data = JSONParser().parse(request)

        #convvert json response to string
        y = json.dumps(item_data)
        chat_prompt = [
        {"role": "user", "content": y}
        ]
   
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_prompt,
            max_tokens = 250
            )

    return JsonResponse({'response': response}, status=status.HTTP_200_OK)
   

