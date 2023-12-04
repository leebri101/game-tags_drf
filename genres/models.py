from django.db import models
from cloudinary.models import CloudinaryField


class Genre(models.Model):
    """Model for genres of games"""
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Genre:',
        help_text=(
            'format: required, max_length=255'
        )
    )
    description = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Description:',
        help_text=(
            'format: not required, max_length=255'
        )
    )
    image = CloudinaryField(
        'image', default='placeholder'
    )
