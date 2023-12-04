from django.contrib import admin
from .models import Game, Genre


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Admin for the games and genre app."""
    list_display = (
        'name', 'description', 'image', 'genre')
    list_filter = ('name', 'genre')
    search_fields = ('name', 'description', 'genre')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'image', 'genre')
        }),
    )

