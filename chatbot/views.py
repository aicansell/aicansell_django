from django.shortcuts import render
from openai import ChatCompletion
import openai
from decouple import config

from rest_framework.decorators import api_view

from django.http import JsonResponse



def chatbot_view(request):
    conversation = request.session.get('conversation', [])

    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # Define your chatbot's predefined prompts
        prompts = []

        # Append user input to the conversation
        if user_input:
            conversation.append({"role": "user", "content": user_input})

        # Append conversation messages to prompts
        prompts.extend(conversation)

        # Set up and invoke the ChatGPT model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompts,
            api_key=config('api_key')

        )
        
        # Extract chatbot replies from the response

        chatbot_replies = [message['message']['content'] for message in response['choices'] if message['message']['role'] == 'assistant']

        # Append chatbot replies to the conversation
        for reply in chatbot_replies:
            conversation.append({"role": "assistant", "content": reply})

        # Update the conversation in the session
        request.session['conversation'] = conversation

        return render(request, 'chat.html', {'user_input': user_input, 'chatbot_replies': chatbot_replies, 'conversation': conversation})
    else:
        request.session.clear()
        return render(request, 'chat.html', {'conversation': conversation})


"""
openai.api_key = config('api_key')

@api_view(['GET'])
def get_completion(prompt):
	print(prompt)
	query = openai.Completion.create(
		engine="text-davinci-003",
		prompt=prompt,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.5,
	)

	response = query.choices[0].text
	print(response)
	return response

@api_view(['POST'])
def query_view(request):
	if request.method == 'POST':
		prompt = request.POST.get('prompt')
		response = get_completion(prompt)
		return JsonResponse({'response': response})
	return response
"""    
      