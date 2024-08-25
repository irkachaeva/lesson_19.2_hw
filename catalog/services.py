from config.settings import CACHE_ENABLED
from catalog.models import Product
from django.core.cache import cache


def get_products_from_cache():
    """получает данные о продуктах из кеша. если кеш пуст, идет в БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
