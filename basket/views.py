from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Basket
from shop.models import Shop, Category


def basket_add(request, product_id):
    product = Shop.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(pk=basket_id, user=request.user)
    basket.delete()
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return redirect('basket:my_basket')


def basket_show(request):
    baskets = Basket.objects.filter(user=request.user)
    categories = Category.objects.all()

    context = {
        'title': 'Моя корзина',
        'baskets': baskets,
        'categories': categories,
    }

    return render(request, 'basket/basket.html', context)


