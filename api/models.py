from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Gamer(AbstractUser):
    username = models.CharField(max_length=40, unique=True, null=True, blank=True)
    email = models.CharField(unique=True, max_length=100)
    steam = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return f"{self.username}"


class Videogame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.title}"


class Party(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
