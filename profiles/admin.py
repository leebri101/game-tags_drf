from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin Display,Filter,Search fields"""
    list_display = (
        'user',
        'user_name',
        'first_name',
        'last_name',
    )
    list_filter = (
        'user',
        'user_name',
        'first_name',
        'last_name',
    )
    search_fields = (
        'user',
        'user_name',
        'first_name',
        'last_name',
    )
