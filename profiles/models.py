from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from games.models import Game


class Profile(models.Model):
    """Model for profiles"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User',
        help_text='Required, unique.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated at'
    )
    user_name = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        verbose_name='Username',
        help_text='Required, max length: 100 characters.'
    )
    first_name = models.CharField(
        max_length=150,
        blank=False,
        null=True,
        verbose_name='First Name',
        help_text='Required, max length: 150 characters.'
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
        null=True,
        verbose_name='Last Name',
        help_text='Required, max length: 150 characters.'
    )
    bio = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Bio',
        help_text='Optional, max length: 255 characters.'
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
        related_name='profiles'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user}'s profile"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Signal receiver to create a profile when a new user is created."""
    if created:
        Profile.objects.create(user=instance)
