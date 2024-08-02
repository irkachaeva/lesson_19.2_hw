from django.urls import path
from blog.apps import AppConfig, BlogConfig
from blog.views import BlogListView, BlogDeleteView, BlogUpdateView, BlogDetailView, BlogCreateView

app_name = BlogConfig.name
#app_name = AppConfig.__name__

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('', BlogListView.as_view(), name='list'),

    ]
