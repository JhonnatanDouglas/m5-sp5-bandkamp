from rest_framework import serializers
from albums.serializers import AlbumSerializer
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "duration",
            "album_id",
        ]
        extra_kwargs = {
            "album_id": {"read_only": True},
        }

    def create(self, validated_data):
        return Song.objects.create(**validated_data)