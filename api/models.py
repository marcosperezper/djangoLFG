from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class Gamer(AbstractUser):
    username = models.CharField(max_length=40, unique=True, null=True, blank=True)
    steam = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return f"{self.username}"


class Videogame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class Party(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    videogame = models.ForeignKey(
        Videogame,
        on_delete=models.CASCADE,
        related_name='parties',
    )
    creator = models.ForeignKey(Gamer,
                                on_delete=models.CASCADE,
                                related_name='parties')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=400, null=True)
    writer = models.ForeignKey(Gamer,
                               on_delete=models.CASCADE,
                               related_name='messages'
                               )
    party = models.ForeignKey(Party,
                              on_delete=models.CASCADE,
                              related_name='party_messages'
                              )
    sent_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        """
        Used to save timestamps on created
        """
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.text}"
