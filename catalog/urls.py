from django.urls import path
from catalog.apps import AppConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, ProductDeleteView
from blog.views import BlogListView
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

app_name = AppConfig.__name__

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('', BlogListView.as_view(), name='view'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),

]



