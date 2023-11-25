from catalog.apps import CatalogConfig
from catalog.views import IndexListView, ContactsView, ProductsListView, CategoryListView
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/products', ProductsListView.as_view(), name='products'),
]
