from django.db.models import Q
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_tracking.mixins import LoggingMixin

from organisation.models import Org, Org_Roles, Weightage
from organisation.serializers import OrgSerializer, OrgRolesSerializer, Weightage

class OrgViewSets(LoggingMixin, ViewSet):
    serializer_class = OrgSerializer
    
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Org, id=pk)


    @staticmethod
    def get_queryset():
        return Org.objects.all()


    def list(self, request):
        serialized_data = self.serializer_class(self.get_queryset(), many=True).data
        response = {
            'status': 'Success',
            'data': serialized_data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, **kwargs):
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'data': self.serializer_class(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
    def create(self, request):
        request_data = self.request.data
        data = {
            'name': request_data.get('name'),
            'description': request_data.get('description'),
            'industry': request_data.get('industry'),
        }
        
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Org was successfully created.'
        }
        return Response(response, status=status.HTTP_201_CREATED)
    

    def update(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        request_data = self.request.data
        
        data = {
            'name': request_data.get('name', instance.name),
            'description': request_data.get('description', instance.description),
            'industry': request_data.get('industry', instance.industry),
        }
        
        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Org was successfully updated.'
        }
        return Response(response, status=status.HTTP_201_CREATED)


    def destroy(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        instance.delete()

        response = {
            'data': '',
            'message': "Successfully deleted Org"
        }
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)
