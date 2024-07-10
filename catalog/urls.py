from django.urls import path
from catalog.apps import AppConfig
from catalog.views import home, contacts
from catalog.views import product_detail, product_list

app_name = AppConfig.__name__

urlpatterns = [
    path('', home, name='home'),
    path('', product_list, name='products_list'),
    path('catalog/<int:pk>', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts')
]



