from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'avatar', 'is_active',
                  'gender', 'latitude', 'longitude', 'distance']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'],
                                        email=validated_data['email'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.avatar = validated_data['avatar']
        user.gender = validated_data['gender']
        user.longitude = validated_data['longitude']
        user.latitude = validated_data['latitude']
        user.is_active = validated_data['is_active']
        return user
