# Registro de evidencias de pruebas

| Fecha | Commit/versión | Entorno | Casos ejecutados | Resultado | Responsable | Archivo de evidencia |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11-01 | Rama local `codex/pizia-checklist`; verificación previa al commit `f523511` | Python 3.14.6, Django 6.0.6, SQLite en BD temporal de pruebas | `manage.py check`; `makemigrations --check --dry-run`; 8 tests automatizados | Correcto: check sin errores, migraciones sincronizadas, 8/8 OK | Codex · completar responsable del equipo | Salida resumida: esta fila; faltan capturas del navegador |

Pendiente: ejecutar los mismos casos con PostgreSQL, capturar pantallas reales del navegador y registrar el commit final del aprendiz.

Guarda aquí capturas reales, sin información personal sensible. No reemplaces “Pendiente” hasta ejecutar y revisar los casos.
