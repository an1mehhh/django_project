from django.shortcuts import render
from catalog.models import Product, Category


def home(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Skystore',
        'description': 'Skystore - это отличный вариант хранения ваших плагинов и примеров кода, который вы бы хотели продать',
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request, pk):
    context = {
        'object_list': Product.objects.filter(category_id=pk)
    }
    return render(request, 'catalog/products.html', context)
