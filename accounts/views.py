
from rest_framework import permissions, status, permissions, generics
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'message':'User created successfully!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(request):
        username = request.data.get('username')
        password = request.ddata.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            })
        return Response({'message': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)
         
class LogoutView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass
        return Response({'message': 'User logged out successfully!'}, status=status.HTTP_200_OK)