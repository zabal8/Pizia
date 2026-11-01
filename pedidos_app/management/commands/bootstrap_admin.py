import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Crea el usuario administrador inicial a partir de variables de entorno."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "").strip()
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "").strip()
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "")
        values = (username, email, password)

        if not any(values):
            self.stdout.write("No se configuró usuario inicial; se omite su creación.")
            return
        if not all(values):
            raise CommandError(
                "Configura DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL y "
                "DJANGO_SUPERUSER_PASSWORD, o deja las tres vacías."
            )

        user_model = get_user_model()
        if user_model.objects.filter(username=username).exists():
            self.stdout.write("El usuario administrador inicial ya existe; no se modificó.")
            return

        user_model.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.stdout.write(self.style.SUCCESS("Usuario administrador inicial creado."))
