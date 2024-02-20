# views.py
from rest_framework import generics, permissions
from rest_framework import viewsets,status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import *
from .models import User
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    
    def create(self, request, *args, **kwargs):
  
        username = request.data.get('username')
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        email = request.data.get('email') 
        
        create_user = User.objects.create_superuser(username=username, phone_number=phone_number, email=email, password=make_password(password))
        serializer = CustomUserSerializer(create_user)

        return Response({'message': 'User and Superuser created successfully'}, status=status.HTTP_201_CREATED)


    