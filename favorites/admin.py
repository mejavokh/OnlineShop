from django.contrib import admin

from .models import *


class FavoritesAdmin(admin.ModelAdmin):
    list_display = ['user', 'products']


admin.site.register(Favorites, FavoritesAdmin)
