from django.contrib import admin
from crud.models import Singer, Album, Song

# Register your models here.

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'singer_name', 'singer_age']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'singer', 'title', 'release_date']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'album', 'song_name', 'duration']

    