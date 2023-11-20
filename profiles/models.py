from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    '''Models for profiles'''
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User',
        help_text=('format: Required, unique=True'
        )
    )
    username = models.CharField(
        max_length=255, blank=True)
    firstname = models.CharField(max_length=200, blank=True)
    lastname = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )
    pronouns = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField()
