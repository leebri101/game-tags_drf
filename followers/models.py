from django.db import models
from odjango.contrib.auth.models import User
from datetime import datetime


class Follower(models.Model):
    """Model for Followers"""
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
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at:',
    )
