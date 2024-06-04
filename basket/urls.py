from django.urls import path
from .views import basket_add, basket_remove, basket_show

app_name = 'basket'

urlpatterns = [
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove_from_basket/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('my_basket/', basket_show, name='my_basket'),
]



