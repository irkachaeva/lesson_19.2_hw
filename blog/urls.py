from django.urls import path
from blog.apps import AppConfig
from blog.views import BlogListView


app_name = AppConfig.__name__

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list')
    ]
