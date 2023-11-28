from django.db import models
from datetime import datetime
from posts.models import Post
from django.contrib.auth.models import User


class Comments(models.Model):
    """Model for comments"""
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Posted at:',
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Updated at:',
    )
    description = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Description:',
        help_text=(
            'format: not required, max_length=255'
        )
    )
