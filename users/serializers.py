from rest_framework import serializers

from accounts.models import Account

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'user_role', 'is_email_confirmed', 'role']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'user_role', 'is_email_confirmed', 'role']
