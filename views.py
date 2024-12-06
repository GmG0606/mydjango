from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import viewsets

from HerritageHub.heritageHub import UserSerializer #type: ignore
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
   