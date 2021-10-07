from .models import Videogame, Gamer, Party, Message
from rest_framework import viewsets, status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import VidegoameSerializer, GamerSerializer, PartySerializer, MessageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


# Create your views here.
@api_view(["GET"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def welcome(request):
    content = {"message": "LFG API welcomes you!"}
    return JsonResponse(content)


class VideogameViewSet(viewsets.ModelViewSet):
    serializer_class = VidegoameSerializer
    queryset = Videogame.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "title"


class GamerViewSet(viewsets.ModelViewSet):
    serializer_class = GamerSerializer
    queryset = Gamer.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PartyViewSet(viewsets.ModelViewSet):
    serializer_class = PartySerializer
    queryset = Party.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MessageListView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, **kwargs):
        party_id = self.kwargs['party_id']
        return Message.objects.filter(party__id=party_id)

    def perform_create(self, serializer, **kwargs):
        party_id = self.kwargs['party_id']
        party = Party.objects.get(pk=party_id)
        serializer.save(writer=self.request.user, party=party)


class GamerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "username"
