from django.contrib import admin

from .models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ['pk', 'city', 'street', 'name', 'house_number', 'opening_time', 'closing_time']

admin.site.register(Shop, ShopAdmin)
