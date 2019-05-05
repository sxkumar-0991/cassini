from django.shortcuts import render
from .serializers import SongsSerializer
from .models import Songs
from rest_framework import generics

class ListSongsView(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


