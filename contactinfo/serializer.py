# serializers.py
from rest_framework import serializers
from .models import *





class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['user','id', 'name', 'email', 'phone_number', 'address']
        read_only_fields = ['user','id']

 
    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Name is required.")
        return data