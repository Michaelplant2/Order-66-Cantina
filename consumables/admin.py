from django.contrib import admin
from .models import Consumable

class ConsumableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'price', 'cuisine_type')
    list_display_links = ('id', 'name')
    list_filter = ('cuisine_type',)
    list_editable = ('is_published',)
    search_fields = ('name', 'description', 'price')
    list_per_page = 25

admin.site.register(Consumable, ConsumableAdmin)