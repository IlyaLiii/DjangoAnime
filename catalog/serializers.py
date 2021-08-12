from rest_framework import serializers
from .models import Anime_title, Genres


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('id', 'genre')
