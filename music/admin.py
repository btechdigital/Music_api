from django.contrib import admin
from .models import Artist, Album, Playlist, Song
# Register your models here.


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Song)