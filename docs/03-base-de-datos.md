# 03 · Base de datos PostgreSQL

El esquema lógico se declara en `pedidos_app/models.py`; Django genera y aplica migraciones. No se crean ni borran tablas manualmente al arrancar. La relación de ingredientes usa una tabla intermedia automática. Restricciones: email único, pedido vinculado a cliente y pizza, pago uno-a-uno con pedido.

Para ejecutar PostgreSQL local: `docker compose up --build`. Compose conserva datos en el volumen `postgres_data`. Para usar un PostgreSQL existente, define `DATABASE_URL` con una URL de conexión y `DJANGO_DEBUG=false`; nunca guardes contraseñas reales en Git.

La aplicación usa SQLite si `DATABASE_URL` no existe para facilitar una demo sin Docker. Esa base local no representa el despliegue final. La estructura visual está en `docs/02-diseno.md`.

## Datos de demostración

`python manage.py seed_demo` inserta ingredientes y pizzas ficticios de forma repetible. No carga clientes ni pedidos personales. El comando puede ejecutarse más de una vez sin crear duplicados por nombre.

## Operación y respaldo

En una instalación PostgreSQL administra respaldo/restauración con `pg_dump`/`pg_restore` y conserva las credenciales en el gestor de secretos del proveedor. No uses el plan efímero de pruebas para datos de producción. El equipo debe verificar el respaldo y restauración antes de usar datos reales.
