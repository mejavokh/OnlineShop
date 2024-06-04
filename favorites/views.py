from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Favorites
from shop.models import Shop, Category


@login_required
def add_to_favorites(request, product_id):
    products = get_object_or_404(Shop, id=product_id)
    Favorites.objects.get_or_create(user=request.user, products=products)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_favorites(request, product_id):
    products = get_object_or_404(Shop, id=product_id)
    favorite = Favorites.objects.filter(user=request.user, products=products)
    favorite.delete()
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return redirect('favorites:favorite_list')


@login_required
def favorite_list(request):
    favorites = Favorites.objects.filter(user=request.user)
    categories = Category.objects.all()

    context = {
        'title': "Избранное",
        'favorites': favorites,
        'categories': categories
    }

    return render(request, 'favorites/favorite_list.html', context)





