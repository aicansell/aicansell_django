from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from assign.models import SeriesAssignUser
from assign.serializers import SeriesAssignUserSerializer, SeriesAssignUserListSerializer

class SeriesAssignUserViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(SeriesAssignUser, pk=pk)
    
    @staticmethod
    def get_queryset():
        return SeriesAssignUser.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = SeriesAssignUserListSerializer(queryset, many=True)
        response = {
            "status": "success",
            "message": "Series Assign User List",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SeriesAssignUserListSerializer(instance)
        response = {
            "status": "success",
            "message": "Series Assign User Detail",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = SeriesAssignUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Series Assign User Created",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "status": "error",
            "message": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SeriesAssignUserSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Series Assign User Updated",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            "status": "error",
            "message": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            "status": "success",
            "message": "Series Assign User Deleted"
        }
        return Response(response, status=status.HTTP_200_OK)
