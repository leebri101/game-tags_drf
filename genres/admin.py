from django.contrib import admin
from .models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin for the genre app."""
    list_display = (
        'name',
        'description',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
    )
