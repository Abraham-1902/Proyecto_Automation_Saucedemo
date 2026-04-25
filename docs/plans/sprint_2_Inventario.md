# 📋 Plan de Pruebas: Módulo de Inventario y Productos (Sprint 2)

## 1. Información General
* **Proyecto:** Automatización SauceDemo (E-commerce)
* **Módulo:** Gestión de Inventario y Visualización de Productos
* **QA Engineer:** Abraham
* **Estado:** 🟢 Activo

---

## 2. Objetivos de la Automatización
Validar la correcta carga, visualización y ordenamiento de los productos en la tienda. Se busca asegurar que la información crítica (nombre, descripción, precio) sea íntegra y que las herramientas de filtro funcionen según los requisitos del negocio.

* **Enfoque:** Page Object Model (POM) para modularidad de elementos de inventario.
* **Estrategia:** Validación de componentes dinámicos y lógica de negocio (ordenamiento).

---

## 3. Precondiciones
1.  **URL de Pruebas:** [https://www.saucedemo.com/inventory.html](https://www.saucedemo.com/inventory.html)
2.  **Sesión Activa:** Requiere un login exitoso previo (**TC001** como pre-requisito).
3.  **Entorno:** Playwright configurado en modo *Sync*.

---

## 4. Matriz de Trazabilidad y Cobertura
| ID | Escenario de Prueba | Prioridad | Tipo | Resultado Esperado |
| :--- | :--- | :--- | :---: | :--- |
| **TC008** | Carga de Productos | Alta | (+) | Visibilidad de al menos 6 productos con datos completos (Nombre, Desc, Precio). |
| **TC009** | Ordenar por Precio (Low to High) | Media | (+) | Lista organizada de menor a mayor precio de forma ascendente. |
| **TC010** | Ordenar por Precio (High to Low) | Media | (+) | Lista organizada de mayor a menor precio de forma descendente. |
| **TC011** | Ordenar por Nombre (A to Z) | Baja | (+) | Lista organizada alfabéticamente de la A a la Z. |
| **TC012** | Ordenar por Nombre (Z to A) | Baja | (+) | Lista organizada alfabéticamente de la Z a la A. |
| **TC013** | Consistencia de Imágenes | Media | (+) | Todas las imágenes de productos deben cargar correctamente (no rotas). |

---

## 5. Configuración del Stack Técnico
| Herramienta | Función |
| :--- | :--- |
| **Playwright** | Manejo de selectores complejos y esperas automáticas. |
| **Pytest** | Manejo de Fixtures para la navegación post-login. |
| **Pytest-HTML** | Registro de evidencias de la carga de inventario. |
| **Python List/Dict** | Procesamiento de datos para validación de lógica de filtros. |

---

## 6. Ejecución y Reportabilidad
Para ejecutar exclusivamente las validaciones de este Sprint y generar el reporte de inventario, utilice:

```bash
pytest tests/test_inventory_load.py --html=reporte_inventario.html --self-contained-html
