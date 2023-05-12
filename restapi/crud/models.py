from django.db import models

# Create your models here.

class Singer(models.Model):
    singer_name = models.CharField(max_length=100)
    singer_age = models.IntegerField()


    def __str__(self):
        return self.singer_name
    

class Album(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title
    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    duration = models.DurationField()


    def __str__(self):
        return self.song_name
    
