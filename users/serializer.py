# serializers.py
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username','phone_number', 'address','password')
        
        extra_kwargs = {
                        "phone_number": {"required": True,},

                    "password": {"write_only": True,"required": False},
                    }
        
    def validate_email(self, value):
            existing_users = User.objects.filter(email=value)
            if self.instance:  
                existing_users = existing_users.exclude(pk=self.instance.pk)

            if existing_users.exists():
                raise serializers.ValidationError("This email address is already in use.")
            
            return value

    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return data


