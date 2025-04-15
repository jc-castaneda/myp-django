from enum import unique
from pyclbr import Class
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):


    # Expanding on the built-in model
    class UserType(models.TextChoices):
        PRODUCER = "1", "Producer"
        MUSICIAN = "2", "Musician"
        SINGER = "3", "Singer"

    username = models.CharField(max_length = 64, unique=True)
    password = models.CharField(max_length = 64)
    email = models.CharField(max_length = 512, unique=True)
    bio = models.CharField(max_length = 512, blank=True, null=True)
    interests = models.JSONField(blank=True, null=True, default=dict)
    skills = models.JSONField(blank=True, null=True, default=dict)
    user_type = models.CharField(max_length = 8, choices = UserType.choices)

    # Returns username
    def __str__(self):
        return self.username
