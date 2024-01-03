from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.permissions import IsAuthenticated

from users.serializers import UsersListSerializer, UsersSerializer
from accounts.models import Account

class UsersViewSet(LoggingMixin, ViewSet):
    permission_classes  = [IsAuthenticated]
    
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Account, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Account.objects.all()
    
    
    def list(self, request):
        if request.user.user_role not in ['admin', 'super_admin']:
            response = {
                'status': "failed",
                'message': "You are not authorized to view this page",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = UsersListSerializer(self.get_queryset(), many=True)
        response = {
            'status': "success",
            'message': "List of users",
            'data': serializer.data,
        }
        
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if request.user.user_role not in ['admin', 'super_admin']:
            response = {
                'status': "failed",
                'message': "You are not authorized to view this page",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        
        user = self.get_object(pk)
        serializer = UsersSerializer(user)
        response = {
            'status': "success",
            'message': "User details",
            'data': serializer.data,
        }
        
        return Response(response, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if request.user.user_role not in ['admin', 'super_admin']:
            response = {
                'status': "failed",
                'message': "You are not authorized to view this page",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        
        user = self.get_object(pk)
        
        request_data  = {
            'first_name': request.data.get('first_name', user.first_name),
            'last_name': request.data.get('last_name', user.last_name),
            'email': request.data.get('email', user.email),
            'username': request.data.get('username', user.username),
            'user_role': request.data.get('user_role', user.user_role),
            'is_email_confirmed': request.data.get('is_email_confirmed', user.is_email_confirmed),
            'role': request.data.get('role', user.role.id),
        }
        
        serializer = UsersSerializer(user, data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': "User updated successfully",
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': "failed",
            'message': "User update failed",
            'data': serializer.errors,
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if request.user.user_role not in ['admin', 'super_admin']:
            response = {
                'status': "failed",
                'message': "You are not authorized to view this page",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        
        user = self.get_object(pk)
        user.delete()
        response = {
            'status': "success",
            'message': "User deleted successfully",
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    