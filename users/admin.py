from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'email']

admin.site.register(User, UserAdmin)
