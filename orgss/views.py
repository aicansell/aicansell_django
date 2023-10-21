from django.db.models import Q
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_tracking.mixins import LoggingMixin

from orgss.models import Org, Org_Roles, Weightage
from orgss.serilaizers import OrgSerializer, OrgRolesSerializer, OrgRolesListSerializer, WeightageSerializer, WeightageListSerializer

class OrgViewSet(LoggingMixin, ViewSet):
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
            'industry': request_data.get('industry', instance.industry.id),
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

class OrgRolesViewSet(LoggingMixin, ViewSet):
    serializer_class = OrgRolesSerializer
    
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Org_Roles, id=pk)


    @staticmethod
    def get_queryset():
        return Org_Roles.objects.all()


    def list(self, request):
        serialized_data = OrgRolesListSerializer(self.get_queryset(), many=True).data
        response = {
            'status': 'Success',
            'data': serialized_data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, **kwargs):
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'data': OrgRolesListSerializer(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
    def create(self, request):
        request_data = self.request.data
        data = {
            'org_role_name': request_data.get('org_role_name'),
            'org': request_data.get('org'),
            'role': request_data.get('role'),
            'subrole': request_data.get('subrole')
        }
        
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Org_Roles was successfully created.'
        }
        return Response(response, status=status.HTTP_201_CREATED)
    

    def update(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        request_data = self.request.data
        
        data = {
            'org_role_name': request_data.get('org_role_name', instance.org_role_name),
            'org': request_data.get('org', instance.org),
            'role': request_data.get('role', instance.role),
            'subrole': request_data.get('subrole', instance.subrole)
        }
        
        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Org_Roles was successfully updated.'
        }
        return Response(response, status=status.HTTP_201_CREATED)


    def destroy(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        instance.delete()

        response = {
            'data': '',
            'message': "Successfully deleted Org_Roles"
        }
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class WeightageViewSet(LoggingMixin, ViewSet):
    serializer_class = WeightageSerializer
    
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Weightage, id=pk)


    @staticmethod
    def get_queryset():
        return Weightage.objects.all()


    def list(self, request):
        serialized_data = WeightageListSerializer(self.get_queryset(), many=True).data
        response = {
            'status': 'Success',
            'data': serialized_data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, **kwargs):
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'data': WeightageListSerializer(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
    def create(self, request):
        request_data = self.request.data
        data = {
            'org_role': request_data.get('org_role'),
            'subcompetency': request_data.get('subcompetency'),
            'weightage': request_data.get('weightage'),
        }
        
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Weightage was successfully created.'
        }
        return Response(response, status=status.HTTP_201_CREATED)
    

    def update(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        request_data = self.request.data
        
        data = {
            'org_role': request_data.get('org_role', instance.org_role),
            'subcompetency': request_data.get('subcompetency', instance.subcompetency),
            'weightage': request_data.get('weightage', instance.weightage),
        }
        
        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'Weightage was successfully updated.'
        }
        return Response(response, status=status.HTTP_201_CREATED)


    def destroy(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        instance.delete()

        response = {
            'data': '',
            'message': "Successfully deleted Weightage"
        }
        
        return Response(response, status=status.HTTP_204_NO_CONTENT)