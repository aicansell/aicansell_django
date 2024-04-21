from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from SnakeLadderGame.models import SnakeLadderGame, SnakeLadderGameResult
from SnakeLadderGame.models import Questions, Options

from SnakeLadderGame.serializers import SnakeLadderGameSerializer, SnakeLadderGameResultSerializer
from SnakeLadderGame.serializers import QuestionsSerializer, OptionsSerializer

class SnakeLadderGameViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(SnakeLadderGame, pk=pk)
    
    @staticmethod
    def get_queryset():
        return SnakeLadderGame.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = SnakeLadderGameSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'List of SnakeLadderGame',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SnakeLadderGameSerializer(instance)
        response = {
            'status': "success",
            'message': 'SnakeLadderGame details',
            'data': serializer.data
        }
        
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            'name': request.data.get('name'),
            'competency': request.data.get('competency'),
            'description': request.data.get('description'),
            'thumbnail': request.data.get('thumbnail')
        }
        
        serializer = SnakeLadderGameSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'SnakeLadderGame created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "error",
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        request_data = {
            'name': request.data.get('name'),
            'competency': request.data.get('competency'),
            'description': request.data.get('description'),
            'thumbnail': request.data.get('thumbnail')
        }
        
        serializer = SnakeLadderGameSerializer(instance, request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'SnakeLadderGame updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': "error",
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': "success",
            'message': 'SnakeLadderGame deleted successfully',
            'data': {}
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    
class QuestionsViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Questions, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Questions.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionsSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'List of Questions',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = QuestionsSerializer(instance)
        response = {
            'status': "success",
            'message': 'Questions details',
            'data': serializer.data
        }
        
        return Response(response, status=status.HTTP_200_OK)
        
    def create(self, request):
        request_data = {
            'snakeladdergame': request.data.get('snakeladdergame'),
            'question': request.data.get('question'),
            'thumbnail': request.data.get('thumbnail'),
            'timer': request.data.get('timer')
        }
        
        serializer = QuestionsSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Questions created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "error",
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        request_data = {
            'snakeladdergame': request.data.get('snakeladdergame'),
            'question': request.data.get('question'),
            'thumbnail': request.data.get('thumbnail'),
            'timer': request.data.get('timer')
        }
        
        serializer = QuestionsSerializer(instance, request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Questions updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': "error",
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': "success",
            'message': 'Questions deleted successfully',
            'data': {}
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    
class OptionsViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Options, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Options.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = OptionsSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'List of Options',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = OptionsSerializer(instance)
        response = {
            'status': "success",
            'message': 'Options details',
            'data': serializer.data
        }
        
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            'question': request.data.get('question'),
            'option': request.data.get('option'),
            'point': request.data.get('point')
        }
        
        serializer = OptionsSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Options created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "error",
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        request_data = {
            'question': request.data.get('question'),
            'option': request.data.get('option'),
            'point': request.data.get('point')
        }
        
        serializer = OptionsSerializer(instance, request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Options updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': "error",
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': "success",
            'message': 'Options deleted successfully',
            'data': {}
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    
class SnakeLadderGameResultViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(SnakeLadderGameResult, pk=pk)
    
    @staticmethod
    def get_queryset():
        return SnakeLadderGameResult.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = SnakeLadderGameResultSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'List of SnakeLadderGameResult',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SnakeLadderGameResultSerializer(instance)
        response = {
            'status': "success",
            'message': 'SnakeLadderGameResult details',
            'data': serializer.data
        }
        
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            'snakeladdergame': request.data.get('snakeladdergame'),
            'user': request.data.get('user'),
            'score': request.data.get('score')
        }
        
        serializer = SnakeLadderGameResultSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'SnakeLadderGameResult created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "error",
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        request_data = {
            'snakeladdergame': request.data.get('snakeladdergame'),
            'user': request.data.get('user'),
            'score': request.data.get('score')
        }
        
        serializer = SnakeLadderGameResultSerializer(instance, request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'SnakeLadderGameResult updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': "error",
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': "success",
            'message': 'SnakeLadderGameResult deleted successfully',
            'data': {}
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
