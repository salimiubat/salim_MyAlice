# urls.py
from django.urls import path,include
from .views import ContactViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register('contact_info', ContactViewSet,basename="contact_info")

urlpatterns = [
    path('', include(router.urls)),


]
