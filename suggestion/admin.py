from django.contrib import admin

from .models import Suggestion

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 25

admin.site.register(Suggestion, SuggestionAdmin)