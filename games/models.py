from django.db import models
from cloudinary.models import CloudinaryField
from genres.models import Genre
from datetime import date


class Game(models.Model):
    """Model for games"""
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Game Name:',
        help_text=(
            'required, (max length is 255)'
        )
    )
    release_date = models.DateField(
        blank=True,
        null=True,
        help_text=(
            'format:, YYYY-MM-DD'
        )
    )
    game_company = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Game Company:',
        help_text=(
            'required, (max length is 255)'
        )
    )
    game_bio = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Game Bio:',
        help_text=(
            'optionl , (max length is 255)'
        )
    )
    genre = models.ForeignKey(
        Genre,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='games'
    )
    image = CloudinaryField(
        'image', default='placeholder'
    )
