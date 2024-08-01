from django.urls import path
from catalog.apps import AppConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView


app_name = AppConfig.__name__

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts')
]



