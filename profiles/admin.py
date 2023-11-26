from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(amdin.ModelAdmin):
    """Profile Admin"""
    list_display = (
        'user',
        'avatar',
        'user_name',
        'first_name',
        'last_name',
        'bio',
    )