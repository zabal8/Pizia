# 04 · Prototipos de interfaz

## Pantalla de inicio

```text
┌ PizIA ─ Inicio | Menú | Nuevo pedido | Pedidos | Recomienda ┐
│ PIZZERÍA ARTESANAL                                         │
│ Una buena pizza empieza por elegir.                        │
│ [Crear pedido] [Encontrar mi pizza]                        │
│ Clientes [n]   Pizzas [n]   Pedidos [n]                    │
│ Favoritas de la casa       tarjetas de producto            │
└────────────────────────────────────────────────────────────┘
```

## Flujo de pedido (cliente)

```text
┌ Nuevo pedido ────────────────────────────────┐
│ Nombre [____________________________]         │
│ Correo [____________________________]         │
│ Pizza  [Seleccionar producto       ▾]         │
│ [Confirmar pedido]                            │
└──────────────────────────────────────────────┘
→ Mensaje de confirmación con número de pedido.
```

## Recomendador

```text
┌ Preferencias ──────────┐  ┌ Opciones para ti ──────────┐
│ Me gusta [___________] │  │ Pizza · afinidad y motivo │
│ Evitar   [___________] │  │ Precio          [Pedir →] │
│ Tope COP [___________] │  │ ...                       │
│ [Recomendar]           │  └───────────────────────────┘
└────────────────────────┘
```

## Gestión de operación

Pantallas de clientes, ingredientes, menú y pedidos dentro de sesión del personal. Las interfaces de catálogo existentes permiten crear/editar/eliminar desde formularios Django; el acceso requiere login. `/admin/` sirve para administración y cuentas del equipo.

Los anteriores son wireframes y la interfaz HTML responsive implementada se encuentra en `templates/`. Para la evidencia evaluable, ejecuta la aplicación en navegador y captura las pantallas reales en `evidencias/prototipos/`.
