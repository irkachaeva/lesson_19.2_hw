from django.urls import path
from catalog.apps import AppConfig
from catalog.views import home, contacts

app_name = AppConfig.__name__

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
