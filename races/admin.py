from django.contrib import admin
from .models import Race, Horse, Jockey, RaceResult

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'distance', 'terrain', 'weather')
    search_fields = ('name', 'location')
    list_filter = ('date', 'terrain', 'weather')

@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'trainer', 'wins', 'losses')
    search_fields = ('name', 'trainer')

@admin.register(Jockey)
class JockeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'win_percentage')
    search_fields = ('name',)

@admin.register(RaceResult)
class RaceResultAdmin(admin.ModelAdmin):
    list_display = ('race', 'horse', 'jockey', 'position', 'time')
    list_filter = ('race', 'position')
