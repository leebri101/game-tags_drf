from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from datetime import datetime


class Like(models.Model):
    """Likes Model"""
    owner = models.ForeignKey(
        User, 
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at:',
    )
