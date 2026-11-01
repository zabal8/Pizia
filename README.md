# PizIA — pedidos y recomendación de pizzas

Aplicación web del proyecto formativo ADSO. La aplicación usa Django para el backend y las vistas HTML; PostgreSQL es el motor previsto para despliegue. En desarrollo local puede usarse SQLite sin cambiar el código. La recomendación es un sistema de recomendación explicable por contenido: puntúa coincidencias entre ingredientes preferidos, excluye ingredientes indicados y respeta un presupuesto. No llama a un servicio externo ni requiere una clave de IA.

## Inicio local

1. Instala Python 3.12 o superior y crea un entorno virtual.
2. `python -m venv .venv` y activa el entorno.
3. `pip install -r requirements.txt`
4. `Copy-Item .env.example .env` (PowerShell) y configura una clave secreta propia.
5. `python manage.py migrate`
6. `python manage.py seed_demo` para cargar menú de demostración.
7. `python manage.py createsuperuser` para crear la cuenta del equipo operador.
8. `python manage.py runserver` y abre http://127.0.0.1:8000.

En PowerShell: `.\.venv\Scripts\Activate.ps1`. El administrador inicia sesión en `/admin/`; las pantallas de gestión de clientes, ingredientes, menú y pedidos requieren personal autenticado. Los clientes pueden consultar el menú, pedir y solicitar recomendaciones sin iniciar sesión.

## PostgreSQL con Docker

Requiere Docker Desktop. Ejecuta `docker compose up --build`; la aplicación quedará en http://localhost:8000 con PostgreSQL persistente en un volumen local. El usuario y contraseña del Compose son solo para desarrollo local. No los reutilices en un servicio público.

## Mapa del código

- `pedidos_app/`: modelos, validaciones, vistas, URLs, administración y pruebas del backend.
- `pizia/`: configuración Django, conexión de base de datos y enrutamiento del proyecto.
- `templates/`: interfaz web responsive servida por Django.
- Los módulos Node/SQLite del ZIP original se excluyen del paquete final porque tenían una inicialización destructiva; la fuente de verdad es Django/PostgreSQL.
- `docs/`: análisis, diseño, prototipos, plan de pruebas, manuales, guion de exposición y trazabilidad de la lista de chequeo.
- `render.yaml` y `Dockerfile`: base de despliegue. Revisa `docs/08-despliegue.md` antes de publicar.

## Roles

- Cliente: consulta el menú, registra un pedido y filtra sugerencias por ingredientes y presupuesto.
- Operador: administra clientes, menú, ingredientes y pedidos desde las pantallas protegidas y `/admin/`.

El sistema es un prototipo formativo, no una pasarela de pagos. El modelo de pagos legado está disponible en administración, pero no procesa transacciones.

## Verificación

`python manage.py check`, `python manage.py test`, y para validar PostgreSQL local `docker compose up --build`. Los casos esperados están en `docs/06-plan-de-pruebas.md`. Registra en `evidencias/pruebas/` capturas propias de la ejecución real antes de marcar esa evidencia como cumplida.
