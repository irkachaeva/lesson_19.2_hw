from django.urls import path
from catalog.apps import AppConfig
from catalog.views import home, contacts
from django.conf import settings
from django.conf.urls.static import static

app_name = AppConfig.__name__

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
