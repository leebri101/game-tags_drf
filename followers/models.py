from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Follower(models.Model):
    """Model for Followers"""
    owner = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='owner_followers'
    )
    followed = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='followed_followers'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at:',
    )
