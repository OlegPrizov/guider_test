from django.contrib import admin

from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

admin.site.register(City, CityAdmin)
