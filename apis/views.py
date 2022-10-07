from django.shortcuts import render
from rest_framework import generics
from db_app.models import Users
from .serializers import UsersSerializer

# Create your views here.
class UsersAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer