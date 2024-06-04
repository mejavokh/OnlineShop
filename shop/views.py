from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import Category, Shop, Comment
from .forms import UserRegistrationForm, UserLoginForm, CommentForm
def main_page(request):
    shops = Shop.objects.all()
    categories = Category.objects.all()

    context = {
        'title': 'Главная страница',
        'categories': categories,
        'shops': shops,
    }

    return render(request, 'shop/main_page.html', context)


def shop_detail(request, product_id):
    product = Shop.objects.get(id=product_id)
    comments = Comment.objects.filter(product=product_id)
    categories = Category.objects.all()

    context = {
        "title": f"Продукт: {product.title}",
        "comments": comments,
        'categories': categories,
        'product': product
    }
    if request.user.is_authenticated:
        context.update({
            "comment_form": CommentForm()
        })

    return render(request, "shop/shop_detail.html", context)



def category_page(request, category_id):
    category = Category.objects.get(id=category_id)
    shops = Shop.objects.filter(category=category)
    categories = Category.objects.all()

    context = {
        'title': category.title,
        'category': category,
        'shops': shops,
        'categories': categories
    }

    return render(request, 'shop/main_page.html', context)


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались !')
            return redirect('main:main_page')
        else:
            messages.error(request, 'Ошибка регистрации !')
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }

    return render(request, 'shop/user_registration.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:main_page')
    else:
        form = UserLoginForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }

    return render(request, 'shop/user_login.html', context)


def user_logout(request):
    logout(request)
    return redirect('main:main_page')


def save_comment(request, product_id):
    product = Shop.objects.get(id=product_id)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.product = product
        comment.save()
        return redirect("main:shop_detail", product_id)
    else:
        return redirect("main:shop_detail", product_id)
