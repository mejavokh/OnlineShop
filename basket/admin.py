from django.contrib import admin

from .models import *


class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']


admin.site.register(Basket, BasketAdmin)
