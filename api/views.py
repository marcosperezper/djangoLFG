from django.shortcuts import render
from .models import Videogame, Gamer, Party, Message
from rest_framework import viewsets
from .serializers import VidegoameSerializer, GamerSerializer, PartySerializer, MessageSerializer


# Create your views here.

class VideogameViewSet(viewsets.ModelViewSet):
    serializer_class = VidegoameSerializer
    queryset = Videogame.objects.all()


class GamerViewSet(viewsets.ModelViewSet):
    serializer_class = GamerSerializer
    queryset = Gamer.objects.all()


class PartyViewSet(viewsets.ModelViewSet):
    serializer_class = PartySerializer
    queryset = Party.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
