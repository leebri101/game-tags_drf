from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date


class Profile(models.Model):
    '''Models for profiles'''
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User',
        help_text=(
            'format: required, unique=True'
        )
    )
    avatar = CloudinaryField(
        'avatar',
        folder='avatars',
        blank=True,
        null=True,
    )
    user_name = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        verbose_name='Username:',
        help_text=(
            'format: required, max_length=100'
        )
    )
    first_name = models.CharField(
        max_length=150,
        blank=False,
        null=True,
        verbose_name='First Name:',
        help_text=(
            'format: not required, max_length=150'
        )
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
        null=True,
        verbose_name='Last Name:',
        help_text=(
            'format: not required, max_length=150'
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
    bio = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Bio:',
        help_text=(
            'format: not required, max_length=255'
        )
    )
    favourite_games = models.ManyToManyField(
        User, related_name='favourite_games'
    )
