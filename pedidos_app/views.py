from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from .models import Cliente
from .forms import ClienteForm
from .models import Ingrediente, Pizza, Pedido


def inicio(request):
    return render(request, 'inicio.html', {
        'clientes_total': Cliente.objects.count(),
        'pizzas': Pizza.objects.prefetch_related('ingredientes').order_by('nombre')[:6],
        'pedidos_total': Pedido.objects.count(),
        'ingredientes_total': Ingrediente.objects.count(),
    })


def crear_pedido(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip().lower()
        pizza_id = request.POST.get('pizza')
        try:
            if len(nombre) < 3:
                raise ValueError('Datos de cliente no válidos')
            validate_email(email)
            pizza = Pizza.objects.get(pk=pizza_id)
            cliente, _ = Cliente.objects.get_or_create(email=email, defaults={'nombre': nombre})
            pedido = Pedido.objects.create(cliente=cliente, pizza=pizza)
            request.session['pedido_confirmado_id'] = pedido.pk
            return redirect('confirmacion_pedido')
        except (Cliente.DoesNotExist, Pizza.DoesNotExist, ValidationError, ValueError, TypeError):
            messages.error(request, 'Revisa el nombre, el correo y la pizza seleccionada.')
    return render(request, 'pedidos/formulario.html', {
        'pizzas': Pizza.objects.order_by('nombre')
    })


def confirmacion_pedido(request):
    pedido_id = request.session.pop('pedido_confirmado_id', None)
    if not pedido_id:
        return redirect('inicio')
    pedido = get_object_or_404(Pedido.objects.select_related('cliente', 'pizza'), pk=pedido_id)
    return render(request, 'pedidos/confirmacion.html', {'pedido': pedido})


@staff_member_required(login_url='/admin/login/')
def lista_pedidos(request):
    pedidos = Pedido.objects.select_related('cliente', 'pizza').order_by('-fecha')
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})


def recomendar(request):
    """Recomendación explicable basada en preferencias e ingredientes; no llama a un LLM externo."""
    resultados = []
    preferidos = {x.strip().casefold() for x in request.GET.get('preferencias', '').split(',') if x.strip()}
    excluir = {x.strip().casefold() for x in request.GET.get('excluir', '').split(',') if x.strip()}
    presupuesto = request.GET.get('presupuesto', '').strip()
    try:
        presupuesto = float(presupuesto) if presupuesto else None
    except ValueError:
        presupuesto = None
    for pizza in Pizza.objects.prefetch_related('ingredientes').all():
        ingredientes = {i.nombre.casefold() for i in pizza.ingredientes.all()}
        if ingredientes & excluir or (presupuesto is not None and float(pizza.precio) > presupuesto):
            continue
        afinidad = len(preferidos & ingredientes)
        resultados.append({'pizza': pizza, 'afinidad': afinidad,
                           'motivo': 'Incluye: ' + ', '.join(sorted(preferidos & ingredientes)) if preferidos & ingredientes else 'Opción disponible dentro de tus filtros.'})
    resultados.sort(key=lambda x: (-x['afinidad'], x['pizza'].precio))
    return render(request, 'recomendaciones.html', {'resultados': resultados[:5],
        'preferencias': request.GET.get('preferencias', ''), 'excluir': request.GET.get('excluir', ''),
        'presupuesto': request.GET.get('presupuesto', '')})


@staff_member_required(login_url='/admin/login/')
def lista_clientes(request):

    clientes = Cliente.objects.all()

    paginator = Paginator(clientes, 10)

    page = request.GET.get('page')

    clientes = paginator.get_page(page)

    return render(
        request,
        'clientes/lista.html',
        {
            'clientes': clientes
        }
    )


@staff_member_required(login_url='/admin/login/')
def crear_cliente(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('lista_clientes')

    else:

        form = ClienteForm()

    return render(
        request,
        'clientes/formulario.html',
        {
            'form': form
        }
    )


@staff_member_required(login_url='/admin/login/')
def editar_cliente(request, pk):

    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    if request.method == 'POST':

        form = ClienteForm(
            request.POST,
            instance=cliente
        )

        if form.is_valid():

            form.save()

            return redirect(
                'lista_clientes'
            )

    else:

        form = ClienteForm(
            instance=cliente
        )

    return render(
        request,
        'clientes/formulario.html',
        {
            'form': form
        }
    )


@staff_member_required(login_url='/admin/login/')
def eliminar_cliente(request, pk):

    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    if request.method == 'POST':

        cliente.delete()

        return redirect(
            'lista_clientes'
        )

    return render(
        request,
        'clientes/eliminar.html',
        {
            'cliente': cliente
        }
    )
from .models import Ingrediente
from .forms import IngredienteForm
@staff_member_required(login_url='/admin/login/')
def lista_ingredientes(request):

    ingredientes = Ingrediente.objects.all()

    return render(
        request,
        'ingredientes/lista.html',
        {
            'ingredientes': ingredientes
        }
    )


@staff_member_required(login_url='/admin/login/')
def crear_ingrediente(request):

    if request.method == 'POST':

        form = IngredienteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'lista_ingredientes'
            )

    else:

        form = IngredienteForm()

    return render(
        request,
        'ingredientes/formulario.html',
        {
            'form': form
        }
    )


@staff_member_required(login_url='/admin/login/')
def editar_ingrediente(request, pk):

    ingrediente = get_object_or_404(
        Ingrediente,
        pk=pk
    )

    if request.method == 'POST':

        form = IngredienteForm(
            request.POST,
            instance=ingrediente
        )

        if form.is_valid():

            form.save()

            return redirect(
                'lista_ingredientes'
            )

    else:

        form = IngredienteForm(
            instance=ingrediente
        )

    return render(
        request,
        'ingredientes/formulario.html',
        {
            'form': form
        }
    )


@staff_member_required(login_url='/admin/login/')
def eliminar_ingrediente(request, pk):

    ingrediente = get_object_or_404(
        Ingrediente,
        pk=pk
    )

    if request.method == 'POST':

        ingrediente.delete()

        return redirect(
            'lista_ingredientes'
        )

    return render(
        request,
        'ingredientes/eliminar.html',
        {
            'ingrediente': ingrediente
        }
    )
from .models import Pizza
from .forms import PizzaForm
def lista_pizzas(request):

    pizzas = Pizza.objects.all()

    return render(
        request,
        'pizzas/lista.html',
        {
            'pizzas': pizzas
        }
    )


@staff_member_required(login_url='/admin/login/')
def crear_pizza(request):

    if request.method == 'POST':

        form = PizzaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'lista_pizzas'
            )

    else:

        form = PizzaForm()

    return render(
        request,
        'pizzas/formulario.html',
        {
            'form': form
        }
    )


@staff_member_required(login_url='/admin/login/')
def editar_pizza(request, pk):

    pizza = get_object_or_404(
        Pizza,
        pk=pk
    )

    if request.method == 'POST':

        form = PizzaForm(
            request.POST,
            instance=pizza
        )

        if form.is_valid():

            form.save()

            return redirect(
                'lista_pizzas'
            )

    else:

        form = PizzaForm(
            instance=pizza
        )

    return render(
        request,
        'pizzas/formulario.html',
        {
            'form': form
        }
    )


@staff_member_required(login_url='/admin/login/')
def eliminar_pizza(request, pk):

    pizza = get_object_or_404(
        Pizza,
        pk=pk
    )

    if request.method == 'POST':

        pizza.delete()

        return redirect(
            'lista_pizzas'
        )

    return render(
        request,
        'pizzas/eliminar.html',
        {
            'pizza': pizza
        }
    )
