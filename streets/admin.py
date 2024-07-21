from django.contrib import admin

from .models import Street

class StreetAdmin(admin.ModelAdmin):
    list_display = ['pk', 'city', 'name']

admin.site.register(Street, StreetAdmin)
