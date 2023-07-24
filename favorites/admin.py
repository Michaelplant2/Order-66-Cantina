from django.contrib import admin

from .models import Favorite

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('consumable_id', 'user_id')
    list_display_links = ('consumable_id', 'user_id')
    search_fields = ('consumable_id', 'user_id')
    list_per_page = 25

admin.site.register(Favorite, FavoriteAdmin)