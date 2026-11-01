# 07 · Manual técnico

## Requisitos

Python 3.12+, pip, Git. Docker Desktop es opcional para PostgreSQL local. Dependencias con versiones acotadas están en `requirements.txt`.

## Instalación de desarrollo

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

SQLite local se crea automáticamente. Para ejecutar contra PostgreSQL, inicia Compose o cambia `DATABASE_URL`; ejecuta migraciones después del cambio. Antes de publicar, genera un secreto aleatorio privado, fija `DJANGO_DEBUG=false` y actualiza host/origen CSRF permitidos.

## Mantenimiento

- Cambios de modelo: `python manage.py makemigrations` y `python manage.py migrate`; agrega la migración generada al control de versiones.
- Verificación: `python manage.py check`; `python manage.py test`.
- Estáticos para servidor: `python manage.py collectstatic --noinput` (el contenedor lo ejecuta durante la construcción).
- El menú demo puede recargarse con `python manage.py seed_demo`.
- No incluir `.env`, bases de datos locales, secretos ni datos personales en commits.
