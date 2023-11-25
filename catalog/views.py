from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from catalog.models import Product, Category


class IndexListView(ListView):
    model = Category
    template_name = 'catalog/index.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Skystore',
        'description': 'Skystore - это отличный вариант хранения ваших плагинов и примеров кода, который вы бы хотели '
                       'продать',
    }


class ContactsView(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    model = Product
    template_name = 'catalog/category.html'
    context_object_name = 'object_list'


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        pk = self.kwargs['pk']
        category = Category.objects.get(pk=pk)
        return Product.objects.filter(category=category)
