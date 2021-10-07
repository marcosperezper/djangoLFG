from rest_framework import serializers
from .models import Videogame, Gamer, Message, Party


class VidegoameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = "__all__"
        lookup_field = "title"
        # extra_kwargs = {"url": {"lookup_field": "title"}}


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        exclude = (
            'groups',
            'last_login',
            'is_superuser',
            'is_staff',
            'date_joined',
            'first_name',
            'last_name',
            'user_permissions',
            'password',
            'is_active',
        )


class PartySerializer(serializers.ModelSerializer):
    videogame = serializers.StringRelatedField()
    creator = serializers.StringRelatedField()

    class Meta:
        model = Party
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Message
        exclude = ('party',)
