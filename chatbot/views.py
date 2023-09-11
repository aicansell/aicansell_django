from django.shortcuts import render
from openai import ChatCompletion
import openai
from decouple import config

from rest_framework.decorators import api_view

from django.http import JsonResponse



openai.api_key = config('api_key')

@api_view(['GET', 'POST'])
def chatresponse(request):
    keep_prompting = True 

    while keep_prompting:
        prompt = input("Please enter your question. Type exit if done:")
        if prompt == "exit":
            keep_prompting = False
        else:
            chat_prompt = [
                {"role": "user", "content": prompt}
            ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_prompt,
            max_tokens = 250
        )


        print(response["choices"][0]["message"]["content"])
        return JsonResponse({'response': response})

    return JsonResponse({})
