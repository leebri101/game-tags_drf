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
            'Text input required, (max is length 255 characters)'
        )
    )
    description = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Description:',
        help_text=(
            'Text input required, (max is length 255 characters)'
        )
    )
    image = CloudinaryField(
        'image', default='placeholder'
    )

    def __str__(self):
        return f'{self.name}'
