from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User = get_user_model()


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     send_mail(
    #         'Welcome to Our Platform',
    #         f'Hello {user.first_name},\n\nThank you for registering on our platform.',
    #         'aleenadevasia31@gmail.com',  # This should match DEFAULT_FROM_EMAIL
    #         [user.email],
    #         fail_silently=False,
    #     )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request=request, username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        user_serializer = UserSerializer(user)

        return Response({
            'refresh': str(refresh),
            'access': access_token,
            'user': user_serializer.data
        }, status=status.HTTP_200_OK)



class AdminLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Debug: Log the received username and password
        print(f"Received username: {username}")
        print(f"Received password: {password}")

        # Authenticate user
        user = authenticate(request=request, username=username, password=password)

        # Debug: Check if the user is None
        if user is None:
            print("Authentication failed: User is None")
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check if user is superuser
        if not user.is_superuser:
            print("Authorization failed: User is not a superuser")
            return Response({'error': 'You are not authorized to access this page'}, status=status.HTTP_403_FORBIDDEN)

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        user_serializer = UserSerializer(user)

        return Response({
            'refresh': str(refresh),
            'access': access_token,
            'user': user_serializer.data
        }, status=status.HTTP_200_OK)









# Create your views here.
