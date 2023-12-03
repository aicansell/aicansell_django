from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from freemium.models import Freemium, Subscription
from freemium.serializers import FreemiumSerializer, SubscriptionSerializer

class FreemiumViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        return get_object_or_404(Freemium, pk=pk)
    
    def get_queryset(self):
        return Freemium.objects.all()

    def list(self, request, *args, **kwargs):
        service = request.query_params.get('service')
        
        if service:
            instance = self.get_object(service)
            
            if instance.amount == 0:
                return Response({'status': 'Success', 'message': 'This service is free'}, status=status.HTTP_200_OK)
            
            try:
                subscription = Subscription.objects.get(user=request.user, service=instance, is_expired=False)
            except Subscription.DoesNotExist:
                return Response({'status': 'Denied', 'message': 'This service is not subscribed'}, status=status.HTTP_200_OK)
            
            if subscription:
                return Response({'status': 'Success', 'message': 'This service is subscribed'}, status=status.HTTP_200_OK)
        else:
            serializer = FreemiumSerializer(self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = FreemiumSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        request_data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'amount': request.data.get('amount'),
            'duration': request.data.get('duration'),
            'access': request.data.get('access')
        }
        
        serializer = FreemiumSerializer(data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Success', 'message': 'Service created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Failed', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = self.get_object(pk)
        
        request_data = {
            'name': request.data.get('name', instance.name),
            'description': request.data.get('description', instance.description),
            'amount': request.data.get('amount', instance.amount),
            'duration': request.data.get('duration', instance.duration),
            'access': request.data.get('access', instance.access)
        }
        
        serializer = FreemiumSerializer(instance, data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Success', 'message': 'Service updated successfully'}, status=status.HTTP_200_OK)
        return Response({'status': 'Failed', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'status': 'Success', 'message': 'Service deleted successfully'}, status=status.HTTP_200_OK)

class SubscriptionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        return get_object_or_404(Subscription, pk=pk)
    
    def get_queryset(self):
        return Subscription.objects.all()

    def list(self, request, *args, **kwargs):
        subscription = self.get_queryset().filter(user=request.user)
        serializer = SubscriptionSerializer(subscription, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = SubscriptionSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        request_data = {
            'user': request.user.id,
            'service': request.data.get('service'),
            'start_date_time': request.data.get('start_date_time'),
            'end_date_time': request.data.get('end_date_time'),
            'is_expired': request.data.get('is_expired')
        }
        
        serializer = SubscriptionSerializer(data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Success', 'message': 'Subscription created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Failed', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = self.get_object(pk)
        
        request_data = {
            'user': request.user.id,
            'service': request.data.get('service', instance.service),
            'start_date_time': request.data.get('start_date_time', instance.start_date_time),
            'end_date_time': request.data.get('end_date_time', instance.end_date_time),
            'is_expired': request.data.get('is_expired', instance.is_expired)
        }
        
        serializer = SubscriptionSerializer(instance, data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Success', 'message': 'Subscription updated successfully'}, status=status.HTTP_200_OK)
        return Response({'status': 'Failed', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'status': 'Success', 'message': 'Subscription deleted successfully'}, status=status.HTTP_200_OK)