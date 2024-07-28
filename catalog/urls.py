from django.urls import path
from catalog.apps import AppConfig
from catalog.views import contacts, product_list
from catalog.views import product_detail

app_name = AppConfig.__name__

urlpatterns = [
    path('', product_list, name='base'),
    #path('products/', product_list, name='product_list'),
    path('catalog/<int:pk>', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts')
]



