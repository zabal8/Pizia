# 06 · Plan de pruebas

Entorno: Python 3.12+, dependencias de `requirements.txt`; ejecutar primero con SQLite y luego con PostgreSQL de Compose. Crea capturas en `evidencias/pruebas/` con fecha y resultado visibles. Los tests automatizados están en `pedidos_app/tests.py`.

| ID | Caso / pasos | Resultado esperado | Evidencia |
| --- | --- | --- | --- |
| PT-01 | Abrir inicio y menú | HTTP 200 y catálogo visible | Captura navegador |
| PT-02 | Enviar pedido con nombre, email y pizza válidos | Se crea pedido y aparece confirmación con número | Captura y registro |
| PT-03 | Repetir pedido con correo existente | Se reutiliza un cliente y se crea otro pedido | Admin/BD |
| PT-04 | Recomendar con ingrediente excluido | Ningún resultado contiene ese ingrediente | Captura |
| PT-05 | Recomendar con tope de precio | Ningún resultado supera el límite | Captura |
| PT-06 | Abrir gestión sin sesión | Redirección a inicio de sesión | Captura |
| PT-07 | Iniciar sesión como personal y editar menú | Cambios guardados y visibles en catálogo | Captura |
| PT-08 | Reiniciar contenedor PostgreSQL | Datos persisten por volumen | Captura terminal y app |
| PT-09 | Ejecutar `python manage.py check` | Sin errores de configuración | Salida de terminal |
| PT-10 | Ejecutar `python manage.py test` | Todos los casos automatizados pasan | Salida de terminal |

## Criterios de salida

Validación local completada: PT-01 a PT-06 y catálogo demo cubiertos por 8 pruebas automatizadas en SQLite; `check` y revisión de migraciones sin errores. PT-07–PT-08 y todas las capturas manuales siguen pendientes. No marcar el plan como aprobado hasta ejecutar los casos restantes en el entorno de entrega y adjuntar evidencias propias. Registrar fecha, commit final, responsable y resultado real en `evidencias/pruebas/registro.md`.
