from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from QuadGame.models import QuadGame, Quadrant, QuadGameResult
from QuadGame.models import Statements, Questions

from QuadGame.serializers import QuadGameSerializer, QuadrantSerializer, QuadGameResultSerializer
from QuadGame.serializers import StatementsSerializer, QuestionsSerializer

class QuadGameListViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return QuadGame.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuadGameSerializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'QuadGame list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

class QuadGameResultViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return QuadGameResult.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuadGameResultSerializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'QuadGameResult list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            'quadgame': request.data.get('quadgame'),
            'user': request.data.get('user'),
            'score': request.data.get('score')
        }
        
        serializer = QuadGameResultSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'QuadGameResult created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                'status': 'error',
                'message': 'QuadGameResult not created',
                'data': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
