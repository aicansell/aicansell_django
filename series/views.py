from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from series.models import Series, Seasons
from assign.models import SeriesAssignUser
from series.serializers import SeriesSerializer, SeriesListSerializer
from series.serializers import SeasonsSerializer, SeasonsListSerializer
from series.serializers import SeasonsListAssignSerializer

class SeriesViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Series, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Series.objects.all()
    
    def list(self, request):
        series_assigned_ids = SeriesAssignUser.objects.filter(user=request.user).values_list('series__id', flat=True)

        queryset = self.get_queryset().filter(sub_org__org=request.user.org).exclude(id__in=series_assigned_ids)
        
        serializer = SeriesListSerializer(queryset, many=True)
        response = {
            "status": "success",
            "message": "Series list",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SeriesListSerializer(instance)
        response = {
            "status": "success",
            "message": "Series detail",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = SeriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Series created",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "status": "error",
            "message": "Series not created",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SeriesSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Series updated",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            "status": "error",
            "message": "Series not updated",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            "status": "success",
            "message": "Series deleted",
            "data": {}
        }
        return Response(response, status=status.HTTP_200_OK)

class SeasonsViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Seasons, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Seasons.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = SeasonsListAssignSerializer(queryset, many=True)
        response = {
            "status": "success",
            "message": "Seasons list",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SeasonsListAssignSerializer(instance)
        response = {
            "status": "success",
            "message": "Seasons detail",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = SeasonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Seasons created",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "status": "error",
            "message": "Seasons not created",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SeasonsSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Seasons updated",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            "status": "error",
            "message": "Seasons not updated",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            "status": "success",
            "message": "Seasons deleted",
            "data": {}
        }
        return Response(response, status=status.HTTP_200_OK)
