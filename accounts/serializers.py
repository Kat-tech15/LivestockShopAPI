from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    
    def create(request, validated_data):
        user = CustomUser.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password']
        )
        RefreshToken.for_user(user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class EmptySerializer(serializers.Serializer):
    pass