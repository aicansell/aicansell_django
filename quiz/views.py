from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import QuizListSerializer, QuizResultSerializer
from .models import Quiz
from rest_framework.decorators import action
from rest_framework import status,viewsets
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#listing quiz question 

@api_view(['GET']) 
def quiz_list(request):
    
    quiz_list = Quiz.objects.all().order_by('-id')
    serializer = QuizListSerializer(quiz_list, many=True)

    # if there is something in items else raise error
    if quiz_list:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def tutorial_detail(request, pk):
    try: 
        quiz_result = Quiz.objects.get(pk=pk) 
    except Quiz.DoesNotExist: 
        return Response({'message': 'The quiz does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    """
    if request.method == 'GET': 
       
        #quiz_result = Quiz.objects.all().order_by('-id')
        serializer = QuizResultSerializer(quiz_result)
        return Response(serializer.data)
       
        if quiz_result:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    """
    if request.method == 'PUT': 
        quiz_data = JSONParser().parse(request) 
        
       
        
        serializer = QuizResultSerializer(quiz_result, data=quiz_data)
        if serializer.is_valid(): 
            
            quiz_result.answer_count = F('answer_count') + 1
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
  
        
   #elif request.method == 'DELETE': 
    #    tutorial.delete() 
     #   return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
