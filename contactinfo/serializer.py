# serializers.py
from rest_framework import serializers
from .models import *





class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['user','id', 'name', 'email', 'phone_number', 'address']
        read_only_fields = ['user','id']

    def validate_email(self, value):
        if Contact.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Name is required.")
        return data