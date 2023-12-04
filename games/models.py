from django.db import models
from cloudinary.models import CloudinaryField
from datetime import date


class Game(models.Model):
    """Model for games"""
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Games Name:',
        help_text=(
            'format: required, max_length=255'
        )
    )
    release_date = models.DateField(
        blank=True,
        null=True
    )
    game_bio = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Game Bio:',
        help_text=(
            'format: not required, max_length=255'
        )
    )
    genre = models.ForeignKey(
        'Genre',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    image = CloudinaryField(
        'image', default='placeholder'
    )
