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
        user_id = request.query_params.get('user')
        services = self.get_queryset()
        if user_id:
            response = {}
            #Filtering out user subscribed services
            subscriptions = Subscription.objects.filter(user=request.user, is_expired=False)
            response['subscriptions'] = SubscriptionSerializer(subscriptions, many=True).data
            response['status'] = 'Success'
            #return response
            return Response(response, status=status.HTTP_200_OK)
        else:
            # If user is not specified, return a list of all services without subscription status
            serializer = FreemiumSerializer(services, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
