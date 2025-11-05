from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    
    def create(request, validated_data):
        user = CustomUser.objects.create_user(
            username= request.validated_data['username'],
            email= request.validated_data['email'],
            password= request.validated_data['password']
        )
        Token.objects.get_or_create(user=user)
        return user

        