from decimal import Decimal

from django.core.management.base import BaseCommand

from pedidos_app.models import Ingrediente, Pizza


class Command(BaseCommand):
    help = 'Carga ingredientes y pizzas de ejemplo sin duplicar registros.'

    def handle(self, *args, **options):
        catalogo = {
            'Queso mozzarella': ('Margarita', Decimal('25000')),
            'Tomate': ('Margarita', Decimal('25000')),
            'Albahaca': ('Margarita', Decimal('25000')),
            'Pepperoni': ('Pepperoni clásica', Decimal('32000')),
            'Champiñones': ('Huerta', Decimal('29000')),
            'Aceitunas': ('Huerta', Decimal('29000')),
            'Pimentón': ('Huerta', Decimal('29000')),
        }
        pizzas = {}
        for ingrediente_nombre, (pizza_nombre, precio) in catalogo.items():
            ingrediente, _ = Ingrediente.objects.get_or_create(nombre=ingrediente_nombre)
            pizza, _ = Pizza.objects.get_or_create(nombre=pizza_nombre, defaults={'precio': precio})
            pizza.ingredientes.add(ingrediente)
            pizzas[pizza_nombre] = pizza
        self.stdout.write(self.style.SUCCESS(f'Menú de demostración listo: {len(pizzas)} pizzas.'))
