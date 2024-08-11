from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='irenkachaeva@gmail.com',
            first_name='Admin',
            last_name='Catalog',
            is_staff=True,
            is_superuser=True
            )
        user.set_password('123Qwerty')
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Superuser "{user.email}" created successfully!'))
