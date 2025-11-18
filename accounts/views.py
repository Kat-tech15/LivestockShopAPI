from rest_framework import permissions, status, permissions, generics
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer, EmptySerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from django.db import connection
from django.http import JsonResponse


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'message':'User created successfully!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user:
            token,created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            })
        return Response({'message': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)
         
class LogoutView(generics.GenericAPIView):
    serializer_class = EmptySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if hasattr(request.user, "auth_token"):
            request.user.auth_token.delete()
            
        return Response({'message': 'User logged out successfully!'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def health_check(request):
    try:
        connection.ensure_connection()
        db_status= "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    return JsonResponse({
        "status": "OK" if db_status == "connected" else "ERROR",
        "database": db_status,
        "version": "v1.0.0",
        "message": "Livestock API is running as expected."

    })