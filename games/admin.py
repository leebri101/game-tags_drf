from django.contrib import admin
from .models import Game, Genre


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Admin for the games app."""
    list_display = (
        'name',
        'release_date',
        'game_bio',
        'image',
        'genre',
    )
    list_filter = (
        'name',
        'release_date',
        'genre',
    )
    search_fields = (
        'name',
        'release_date',
        'genre',
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin for the genre app."""
    list_display = (
        'name',
        'description',
        'image',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
    )
