from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Posted at:',
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Updated at:',
    )
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Title:',
        help_text=(
            'format: not required, max_length=255'
        )
    )
    description = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Description of Post:',
        help_text=(
            'format: not required, max_length=255'
        )
    )
    image = CloudinaryField(
        'image', default='placeholder'
    )
