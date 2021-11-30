from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'avatar', 'is_active', 'is_staff',
                  'is_superuser',
                  'gender', 'latitude', 'longitude', 'distance']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
