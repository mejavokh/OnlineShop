from django.urls import path

from .views import *


app_name = 'main'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('category/<int:category_id>/', category_page, name='category_page'),
    path('registration/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('shop_detail<int:product_id>/', shop_detail, name='shop_detail'),
    path('save_comment/<int:product_id>/', save_comment, name='save_comment')
]
