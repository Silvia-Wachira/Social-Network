from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from core.user.serializers import UserSerializer
from core.user.models import User

class UserViewset(viewsets.ModelViewSet):
    http_method_names = ('patch', 'get')