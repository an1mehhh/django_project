from blog.apps import BlogConfig
from django.urls import path

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('blog_list/', BlogListView.as_view(), name='list'),
    path('detail/<int:pk>/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/<slug:slug>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete')
]
