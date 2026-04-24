# 📋 Plan de Pruebas: Módulo de Autenticación (Sprint 1)

## 1. Información General
* **Proyecto:** Automatización SauceDemo (E-commerce)
* **Módulo:** Login / Seguridad y Control de Acceso
* **QA Engineer:** Abraham
* **Estado:** 🟢 Activo

---

## 2. Objetivos de la Automatización
Asegurar la integridad del flujo de acceso mediante pruebas de regresión automáticas, validando tanto el flujo positivo (Happy Path) como el manejo de errores y seguridad (Negative Testing).

* **Enfoque:** Page Object Model (POM) para alta mantenibilidad.
* **Estrategia:** Data-Driven Testing (DDT) para escalabilidad de escenarios.

---

## 3. Precondiciones
1.  **URL de Pruebas:** [https://www.saucedemo.com/](https://www.saucedemo.com/)
2.  **Entorno:** Python 3.x con dependencias instaladas (`requirements.txt`).
3.  **Data Source:** Archivo `data/login_data.json` correctamente configurado.

---

## 4. Matriz de Trazabilidad y Cobertura
| ID | Escenario de Prueba | Prioridad | Tipo | Resultado Esperado |
| :--- | :--- | :--- | :---: | :--- |
| **TC001** | Autenticación Exitosa | Alta | (+) | Redirección a `/inventory.html` y visibilidad del header. |
| **TC002** | Usuario Incorrecto | Media | (-) | Mensaje: *Username and password do not match*. |
| **TC003** | Contraseña Incorrecta | Media | (-) | Mensaje: *Username and password do not match*. |
| **TC004** | Campo Usuario Vacío | Baja | (-) | Mensaje: *Username is required*. |
| **TC005** | Campo Contraseña Vacío | Baja | (-) | Mensaje: *Password is required*. |
| **TC006** | Ambos Campos Vacíos | Baja | (-) | Mensaje: *Username is required*. |
| **TC007** | Usuario Bloqueado | Alta | (-) | Mensaje: *Sorry, this user has been locked out*. |

---

## 5. Configuración del Stack Técnico
| Herramienta | Función |
| :--- | :--- |
| **Playwright** | Automatización del navegador (Motor principal). |
| **Pytest** | Orquestador de pruebas y validaciones (Assertions). |
| **Pytest-HTML** | Generación de reportes técnicos con evidencia visual. |
| **JSON** | Gestión de datos desacoplada del código. |

---

## 6. Ejecución y Reportabilidad
Las pruebas están configuradas mediante el archivo `pytest.ini`. Para ejecutar el conjunto completo y generar el reporte técnico, utilice:

```bash
pytest
