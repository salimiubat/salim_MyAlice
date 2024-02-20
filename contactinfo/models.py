from django.db import models
from users.models import *

class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_contact")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)