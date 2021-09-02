from django.shortcuts import render
from .models import Videogame, Gamer
from rest_framework import viewsets
from .serializers import VidegoameSerializer, GamerSerializer


# Create your views here.

class VideogameViewSet(viewsets.ModelViewSet):
    serializer_class = VidegoameSerializer
    queryset = Videogame.objects.all()


class GamerViewSet(viewsets.ModelViewSet):
    serializer_class = GamerSerializer
    queryset = Gamer.objects.all()
