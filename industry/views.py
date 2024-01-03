from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_tracking.mixins import LoggingMixin

from industry.models import Industry
from industry.serializers import IndustrySerializer


class IndustryViewSet(LoggingMixin, ViewSet):
    serializer_class = IndustrySerializer
    
    @staticmethod
    def get_object(pk):
        # Get an Industry object by its primary key (id) or return 404 if not found
        return get_object_or_404(Industry, id=pk)
    
    @staticmethod
    def get_queryset():
        # Return all Industry objects
        return Industry.objects.all()
    
    def list(self, request):
        # Retrieve a list of all Industry objects, serialize them, and return as a response
        serializer_data = self.serializer_class(self.get_queryset(), many=True).data
        response = {
            'status': 'Success',
            'data': serializer_data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, **kwargs):
        # Retrieve a single Industry object by primary key (pk), serialize it, and return as a response
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'data': self.serializer_class(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        # Create a new Industry object from request data, validate it, and return as a response
        request_data = self.request.data
        data = {
            'industry_name': request_data.get('industry_name'),
            'industry_description': request_data.get('industry_description'),
        }
        
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': "Industry data saved successfully"
        }
        return Response(response, status=status.HTTP_201_CREATED)
    
    def update(self, request, **kwargs):
        # Update an existing Industry object, validate it, and return as a response
        instance = self.get_object(kwargs.pop('pk'))
        request_data = self.request.data
        
        data = {
            'industry_name': request_data.get('industry_name', instance.industry_name),
            'industry_description': request_data.get('industry_description', instance.industry_description),
        }
        
        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Industry was successfully updated.'
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def destroy(self, request, **kwargs):
        # Delete an existing Industry object and return a success response
        instance = self.get_object(kwargs.pop('pk'))
        instance.delete()

        response = {
            'data': '',
            'message': "Successfully deleted Industry"
        }
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)
