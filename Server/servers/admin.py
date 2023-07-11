from django.contrib import admin
from .models import Server

class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Server, ServerAdmin)