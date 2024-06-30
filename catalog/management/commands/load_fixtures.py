from django.core.management import BaseCommand, call_command
from django.conf import settings

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        call_command('loaddata', 'catalog.json')