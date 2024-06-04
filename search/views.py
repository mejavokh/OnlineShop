from django.shortcuts import render

from shop.models import Shop
from .forms import SearchForm


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Shop.objects.filter(title__icontains=query)
        else:
            form = SearchForm()
            products = Shop.objects.none()
    else:
        form = SearchForm()
        products = Shop.objects.none()

    context = {
        'form': form,
        'products': products,
        'title': 'Поиск товаров'
    }

    return render(request, 'search/search.html', context)



