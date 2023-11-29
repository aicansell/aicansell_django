from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from freemium.models import Freemium, Subscription
from accounts.models import Account;
from django.shortcuts import get_object_or_404
from rest_framework import status

from freemium.serializers import FreemiumSerializer

class FreemiumViewSet(ViewSet):
    def get_object(self, pk):
        return get_object_or_404(Freemium, pk=pk)
    
    def get_queryset(self):
        return Freemium.objects.all()

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('user', None)
        services = self.get_queryset()
        if user_id is not None:
            # If user is specified, include subscription status for each service
            try:
                user = Account.objects.get(pk=user_id)
            except Account.DoesNotExist:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            serialized_data = []

            for service in services:
                subscription = Subscription.objects.filter(user=user, service=service, is_expired=False).first()
                serializer = FreemiumSerializer(service)

                data = serializer.data
                data['is_subscribed'] = subscription is not None
                data['start_date'] = subscription.start_date if subscription else None
                data['end_date'] = subscription.end_date if subscription else None
                serialized_data.append(data)

            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            # If user is not specified, return a list of all services without subscription status
            serializer = FreemiumSerializer(services, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
