from django.urls import path

from .views import *

app_name = 'favorites'

urlpatterns = [
    path('product/<int:product_id>/add_to_favorites/', add_to_favorites, name='add_to_favorites'),
    path('product/<int:product_id>/remove_from_favorites/', remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', favorite_list, name='favorite_list'),
]




