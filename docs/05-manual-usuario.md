# 05 · Manual de usuario

## Cliente

1. Abre la página de inicio y entra a **Menú** para consultar productos y precios.
2. En **PizIA recomienda**, escribe ingredientes separados por coma, ingredientes que deseas evitar y un presupuesto máximo. Pulsa **Recomendar**. Las opciones muestran coincidencias y el motivo; no se mostrarán pizzas que incluyan ingredientes excluidos.
3. Pulsa **Nuevo pedido**, escribe nombre y correo, selecciona una pizza y confirma. El sistema presenta el número del pedido.

## Operador

1. El responsable crea la cuenta del equipo con `python manage.py createsuperuser`.
2. Inicia sesión en `/admin/`. Usa las pantallas de gestión del menú, ingredientes y clientes o el panel administrativo.
3. Abre **Pedidos** para consultar cliente, pizza y hora de registro.
4. Cierra sesión desde el panel cuando termine.

## Mensajes y limitaciones

Si la recomendación no encuentra opciones, retira algún filtro o revisa el menú. Si el catálogo está vacío, un operador debe cargar productos primero. El pedido no es una compra pagada ni incluye estado de preparación o entrega. Para corregir un correo/nombre de cliente, el operador debe editar el registro desde gestión.
