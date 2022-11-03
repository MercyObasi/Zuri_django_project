
from rest_framework import serializers
from .models import Artiste, Song, Lyric

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Artiste
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'
        
        def __str__(self):
            return "{} - {}".format(self.song.title, self.song.artiste)