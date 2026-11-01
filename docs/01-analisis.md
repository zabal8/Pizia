# 01 · Análisis del proyecto PizIA

**Programa:** Tecnólogo en Análisis y Desarrollo de Software (ADSO)  
**Producto:** sistema web para consulta de menú, registro de pedidos y recomendación de pizzas.  
**Estado:** versión formativa funcional en construcción; completar los datos del grupo y la ficha antes de entregar.

## Problema

Una pizzería pequeña necesita centralizar su menú, clientes y pedidos, y facilitar que el cliente elija un producto de acuerdo con sus gustos, ingredientes que desea evitar y presupuesto. La base recibida tenía módulos de API y pantallas sin conexión entre sí, dos motores de datos incompatibles y una rutina Node que eliminaba tablas al iniciar.

## Objetivo y alcance

Construir una aplicación web que presente el catálogo, permita registrar pedidos asociados a un cliente y ofrezca recomendaciones transparentes a partir de ingredientes y presupuesto. El personal autenticado administra los registros desde el sitio y el panel Django.

Fuera de alcance: cobro en línea, inventario, domicilios, notificaciones, aplicación móvil, aprendizaje de un modelo con datos reales e integración con un proveedor de IA generativa. Los datos de ejemplo son ficticios.

## Actores

| Actor | Necesidad | Permisos |
| --- | --- | --- |
| Cliente | Explorar menú, pedir y descubrir opciones | Inicio, menú, nuevo pedido y recomendaciones |
| Operador de pizzería | Mantener el catálogo y consultar clientes/pedidos | Autenticación Django; CRUD y administración |

## Requisitos funcionales

| ID | Requisito | Criterio de aceptación |
| --- | --- | --- |
| RF-01 | Mostrar inicio y catálogo disponibles | El cliente puede consultar el menú publicado |
| RF-02 | Crear pedido con nombre, correo y pizza | Se conserva el cliente y pedido y se confirma el número |
| RF-03 | Evitar duplicar cliente por correo | Un correo existente reutiliza el mismo registro |
| RF-04 | Recomendar según gusto, exclusiones y tope de precio | Se excluye toda pizza que incumpla un filtro y se explica la coincidencia |
| RF-05 | Gestionar clientes, ingredientes y pizzas | Solo personal autenticado accede a las rutas de gestión |
| RF-06 | Consultar pedidos | Lista del personal con cliente, producto y fecha |
| RF-07 | Mantener datos tras reinicio | PostgreSQL persiste en el volumen/servicio configurado |

## Requisitos no funcionales

| ID | Requisito |
| --- | --- |
| RNF-01 | Interfaz adaptable a móvil y escritorio, idioma español |
| RNF-02 | Claves y URL de base de datos se configuran por variables de entorno |
| RNF-03 | PostgreSQL para despliegue; SQLite permitido solo para desarrollo rápido |
| RNF-04 | Protección CSRF para formularios y acceso de personal autenticado a gestión |
| RNF-05 | Componentes separados por responsabilidad y migraciones Django |
| RNF-06 | Recomendación determinística, explicable y sin enviar preferencias a terceros |

## Historias de usuario

- **HU-01 Cliente:** Como cliente quiero filtrar pizzas por ingredientes y presupuesto para tomar una decisión informada.
- **HU-02 Cliente:** Como cliente quiero registrar mi pedido y recibir confirmación para no depender de una llamada.
- **HU-03 Operador:** Como operador quiero mantener pizzas e ingredientes para que el menú mostrado sea vigente.
- **HU-04 Operador:** Como operador quiero revisar pedidos y clientes para coordinar la atención.
- **HU-05 Operador:** Como operador quiero que las pantallas administrativas exijan inicio de sesión para proteger los datos.

## Supuestos y riesgos

Los nombres y precios del menú de demostración son ilustrativos y deben reemplazarse por información autorizada del equipo. La recomendación solo compara cadenas de ingredientes registrados; no interpreta lenguaje natural ni garantiza ausencia de contaminación cruzada. El despliegue debe usar secretos propios y respaldos si almacena información real.
