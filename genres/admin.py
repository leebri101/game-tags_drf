from django.contrib import admin
from .models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre Admin Display,Filter,Search fields"""
    list_display = (
        'name',
        'description',
        'image',
    )
    list_filter = (
        'name',
        'description',
    )
    search_fields = (
        'name',
        'description'
    )
