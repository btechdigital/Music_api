from django.db import models



class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
    	return self.first_name

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    about_album = models.TextField(null=True, blank=True)

    def __str__(self):
    	return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField('Song', related_name='playlists')

    def __str__(self):
    	return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE, null=True, blank=True)
    about_song = models.TextField(null=True, blank=True)

    def __str__(self):
    	return self.title