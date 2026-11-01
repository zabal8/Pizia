from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from django.contrib.auth import get_user_model
from io import StringIO
from unittest.mock import patch

from .models import Cliente, Ingrediente, Pizza, Pedido


class FlujoClienteTests(TestCase):
    def setUp(self):
        queso = Ingrediente.objects.create(nombre='Queso')
        tomate = Ingrediente.objects.create(nombre='Tomate')
        self.pizza = Pizza.objects.create(nombre='Margarita', precio='25000')
        self.pizza.ingredientes.add(queso, tomate)

    def test_inicio_y_menu_responden(self):
        self.assertEqual(self.client.get(reverse('inicio')).status_code, 200)
        self.assertEqual(self.client.get(reverse('lista_pizzas')).status_code, 200)

    def test_cliente_registra_pedido(self):
        response = self.client.post(reverse('crear_pedido'), {
            'nombre': 'Ana Pérez', 'email': 'ana@example.com', 'pizza': self.pizza.pk,
        })
        self.assertRedirects(response, reverse('confirmacion_pedido'))
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().email, 'ana@example.com')

    def test_correo_existente_reutiliza_cliente(self):
        datos = {'nombre': 'Ana Pérez', 'email': 'ana@example.com', 'pizza': self.pizza.pk}
        self.client.post(reverse('crear_pedido'), datos)
        self.client.post(reverse('crear_pedido'), datos)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Pedido.objects.count(), 2)

    def test_recomendacion_respeta_ingrediente_excluido(self):
        response = self.client.get(reverse('recomendar'), {'excluir': 'tomate'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Margarita')

    def test_recomendacion_respeta_presupuesto(self):
        response = self.client.get(reverse('recomendar'), {'presupuesto': '10000'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Margarita')

    def test_gestion_requiere_personal(self):
        response = self.client.get(reverse('lista_clientes'))
        self.assertEqual(response.status_code, 302)

    def test_correo_invalido_no_registra_pedido(self):
        response = self.client.post(reverse('crear_pedido'), {
            'nombre': 'Ana Pérez', 'email': 'correo-invalido', 'pizza': self.pizza.pk,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Cliente.objects.count(), 0)
        self.assertEqual(Pedido.objects.count(), 0)

    def test_catalogo_demo_se_puede_cargar_dos_veces(self):
        call_command('seed_demo', stdout=StringIO())
        call_command('seed_demo', stdout=StringIO())
        self.assertEqual(Pizza.objects.count(), 3)


class BootstrapAdminTests(TestCase):
    @patch.dict('os.environ', {
        'DJANGO_SUPERUSER_USERNAME': 'operador-inicial',
        'DJANGO_SUPERUSER_EMAIL': 'operador@example.com',
        'DJANGO_SUPERUSER_PASSWORD': 'local-test-password-93x',
    })
    def test_crea_el_administrador_inicial_sin_reemplazarlo(self):
        call_command('bootstrap_admin', stdout=StringIO())
        usuario = get_user_model().objects.get(username='operador-inicial')
        self.assertTrue(usuario.is_superuser)
        self.assertTrue(usuario.check_password('local-test-password-93x'))

        with patch.dict('os.environ', {'DJANGO_SUPERUSER_PASSWORD': 'otra-clave'}):
            call_command('bootstrap_admin', stdout=StringIO())

        usuario.refresh_from_db()
        self.assertTrue(usuario.check_password('local-test-password-93x'))
