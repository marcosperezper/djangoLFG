from rest_framework import serializers
from .models import Videogame, Gamer


class VidegoameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = "__all__"


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
