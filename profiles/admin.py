from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(amdin.ModelAdmin):
    """Profile Admin Display"""
    list_display = (
        'user',
        'avatar',
        'user_name',
        'first_name',
        'last_name',
        'bio',
    )
    list_filter = (
        'user',
        'avatar',
        'user_name',
        'first_name',
        'last_name',
        'bio',
    )
    search_fields = (
        'user',
        'avatar',
        'user_name',
        'first_name',
        'last_name',
        'bio',
    )
