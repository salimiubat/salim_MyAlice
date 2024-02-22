# views.py
from rest_framework import viewsets,status
from .serializer import *
from rest_framework.response import Response


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(user=user)

