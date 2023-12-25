from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from games.models import Game
from datetime import date


class Profile(models.Model):
    """Models for profiles"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User',
        help_text=(
            'format: required, unique=True'
        )
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at:',
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Updated at:',
    )
    user_name = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        verbose_name='Username:',
        help_text=(
            'Text input REQUIRED, (max is length 100 characters)'
        )
    )
    first_name = models.CharField(
        max_length=150,
        blank=False,
        null=True,
        verbose_name='First Name:',
        help_text=(
            'Text input REQUIRED, (max is length 150 characters)'
        )
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
        null=True,
        verbose_name='Last Name:',
        help_text=(
            'Text input REQUIRED, (max is length 150 characters)'
        )
    )
    bio = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Bio:',
        help_text=(
            'Text input optional, (max is length 255 characters)'
        )
    )
    avatar = CloudinaryField(
        'avatar',
        folder='avatars',
        blank=True,
        null=True,
    )
    favourite_games = models.ManyToManyField(
        Game,
        blank=True,
        related_name='profile'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
