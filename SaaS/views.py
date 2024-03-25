from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from SaaS.models import Feature, FeatureList, SaaS
from SaaS.serializers import FeatureSerializer, FeaturesListSerializer
from SaaS.serializers import SaaSSerializer, SaaSListSerializer

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
