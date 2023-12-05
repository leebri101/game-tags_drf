from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Admin for the games app."""
    list_display = (
        'name',
        'release_date',
        'game_company',
        'game_bio',
        'image',
        'genre',
    )
    list_filter = (
        'name',
        'release_date',
        'game_company',
        'genre',
    )
    search_fields = (
        'name',
        'release_date',
        'game_company',
        'genre',
    )
