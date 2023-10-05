from rest_framework import serializers
from rest_framework_tracking.models import APIRequestLog


class TransactionsSerializer(serializers.ModelSerializer):
    requested_at = ""

    class Meta:
        model = APIRequestLog
        fields = ['id', 'user', 'requested_at', 'remote_addr', 'path', 'status_code']