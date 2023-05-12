from rest_framework import serializers
from crud.models import Singer, Album, Song

class SingerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'singer_name', 'singer_age']
        
    def validate_singer_name(self, value):

        if Singer.objects.filter(singer_name=value).exists:
            raise serializers.ValidationError("Singer Alreday Exists")
        return value

class AlbumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'singer', 'title', 'release_date']

    def validate(self, value):
        if Album.objects.filter(title=value).exists:
            raise serializers.ValidationError("Album alreday exists")
        return value
    
    
class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'album', 'song_name', 'duration']
        