# 08 · Despliegue y entrega

## Despliegue de prueba con Render

El repositorio incluye `render.yaml` como Blueprint Docker con servicio web y PostgreSQL. Publica primero el código en un repositorio del aprendiz, conéctalo desde Render y aplica el Blueprint. Configura `DJANGO_ALLOWED_HOSTS` con el dominio exacto asignado y `CSRF_TRUSTED_ORIGINS` con `https://<dominio>`. Crea la cuenta inicial desde consola con `python manage.py createsuperuser` o prepara un procedimiento seguro de bootstrap. Verifica home, catálogo, formularios, login y persistencia tras redeploy.

El plan gratuito de PostgreSQL de Render es temporal (la documentación del proveedor indica expiración a 30 días) y no debe almacenar información de producción. Revisa límites/costos y política vigentes antes de habilitarlo. [Documentación de despliegue Django de Render](https://render.com/docs/deploy-django), [límites de planes gratuitos](https://render.com/docs/free).

## GitHub colaborativo

El directorio tiene un solo repositorio Django; `pedidos_app/` y `pizia/` son backend y `templates/` es la interfaz. Crea un repositorio bajo la cuenta del aprendiz, añade a cada integrante como colaborador, trabaja por ramas y registra aportes reales mediante commits revisables. No inventes commits o integrantes. En este entorno no hay conexión autenticada a GitHub ni remoto configurado, así que la publicación y colaboración deben hacerse desde la cuenta del aprendiz.

## Drive y video

Sube el ZIP/proyecto, documentación, capturas, diapositivas y video a una carpeta cuyo propietario sea el aprendiz. Habilita lectura para los evaluadores según la instrucción oficial y prueba el enlace en ventana privada. Graba la sustentación con cámara encendida; máximo 20 minutos. Un guion sugerido está en `09-guion-presentacion.md`.

La app no puede crear el Drive público, publicar el repositorio o grabar la presentación por el aprendiz desde esta sesión. No marques esos requisitos como cumplidos hasta completar y comprobar esos pasos externos.
