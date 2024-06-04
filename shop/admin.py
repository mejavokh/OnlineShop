from django.contrib import admin

from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    search_fields = ('title', 'description')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super(ShopAdmin, self).save_model(
            request, obj, form, change
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'description')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category)
admin.site.register(Comment)



