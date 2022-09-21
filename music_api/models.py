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
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    url = models.URLField()
    # uploaded_by = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

