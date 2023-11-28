from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from datetime import datetime


class Like(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    followed = models.ForeignKey
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at:',
    )
