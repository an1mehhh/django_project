from catalog.views import home, contacts
from django.urls import path

urlpatterns = [
    path('', home),
    path('contacts', contacts, name='contacts')
]