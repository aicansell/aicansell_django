from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from SaaS.models import Feature, FeatureList, SaaS
from SaaS.serializers import FeatureSerializer, FeaturesListSerializer
from SaaS.serializers import SaaSSerializer, SaaSListSerializer
from sean.models import ItemResult

class FeatureViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Feature, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Feature.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = FeaturesListSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'Features List',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = FeaturesListSerializer(instance)
        response = {
            'status': "success",
            'message': 'Feature Details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

class SaaSViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(SaaS, pk=pk)
    
    @staticmethod
    def get_queryset():
        return SaaS.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = SaaSListSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'SaaS List',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SaaSListSerializer(instance)
        response = {
            'status': "success",
            'message': 'SaaS Details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = SaaSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'SaaS Created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "error",
            'message': 'SaaS Not Created',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class LevelAccessCheck(ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        types = request.query_params.get('types', None)
        try:
            level = int(request.query_params.get('level', None))
            if level < 1:
                response = {
                    'status': "error",
                    'message': 'Level must be greater than 0',
                    'data': None
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response = {
                'status': "error",
                'message': 'Level must be an integer',
                'data': None
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        if not types or not level:
            response = {
                'status': "error",
                'message': 'Types and Level are required',
                'data': None
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        if level is 1:
            response = {
                'status': "success",
                'message': 'Access Granted',
                'data': None
            }
            return Response(response, status=status.HTTP_200_OK)
        
        if types == "item":
            queryset = ItemResult.objects.filter(user=request.user, item__level=level-1)
            sum = 0
            for result in queryset:
                sum += result.score
            if sum >= 70:
                response = {
                    'status': "success",
                    'message': 'Access Granted',
                    'data': {
                        'score': sum 
                    }
                }
                return Response(response, status=status.HTTP_200_OK)
            response = {
                'status': "error",
                'message': 'Access Denied',
                'data': {
                    'score': sum,
                    'level': level-1,
                    'score_needed': 70-sum,
                }
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
