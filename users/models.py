from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    email = models.EmailField(_("электронная почта"), unique=True)
    phone = models.CharField(max_length=35, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар')
    country = models.CharField(max_length=50, verbose_name='Страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
