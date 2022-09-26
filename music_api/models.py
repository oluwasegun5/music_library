from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username



class Song(models.Model):
    SONG_CATEGORY = (
        ('GOSPEL','gospel'),
        ('HIPPOP','hippop'),
        ('JUJU','juju'),
    )
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    uploaded_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=8, choices=SONG_CATEGORY)
    song_url = models.URLField()
    image_url = models.URLField()
    # uploaded_by = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    song = models.ManyToManyField(Song)


