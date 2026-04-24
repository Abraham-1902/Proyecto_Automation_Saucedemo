# 🧪 Proyecto de Automatización: SauceDemo

Este repositorio contiene un framework de pruebas automatizadas profesional desarrollado para la plataforma **SauceDemo**. El proyecto utiliza **Python** y **Playwright**, aplicando el patrón de diseño **Page Object Model (POM)** para garantizar un código limpio, mantenible y escalable.

---

## 🏗️ Arquitectura del Proyecto
El framework está organizado para separar la lógica de los elementos de la interfaz de la lógica de las pruebas:

* **`pages/`**: Contiene las clases de las páginas (Locators y Acciones).
* **`tests/`**: Scripts de prueba que ejecutan los escenarios de validación.
* **`data/`**: Gestión de datos de prueba mediante archivos JSON (Data-Driven Testing).
* **`pytest.ini`**: Configuración centralizada del runner (Modo visible, SlowMo y Reportes).
* **`conftest.py`**: Configuración de fixtures globales para la inicialización del navegador.

---

## 🛠️ Stack Tecnológico
| Herramienta | Uso |
| :--- | :--- |
| **Python 3.x** | Lenguaje de programación principal. |
| **Playwright** | Motor de automatización para interacciones web modernas. |
| **Pytest** | Framework de pruebas para orquestar la ejecución y assertions. |
| **Pytest-HTML** | Generador de reportes visuales detallados en formato HTML. |

---

## 🚀 Configuración y Ejecución Técnica

### 1. Preparación del Entorno
Clona el proyecto y configura el entorno virtual para aislar las dependencias:
```bash
git clone [https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git](https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git)
cd Proyecto_Automation_Saucedemo
python -m venv venv
.\venv\Scripts\activate  # Comando para Windows

pip install pytest-playwright pytest-html
playwright install chromium

# Ejecutar todos los tests y generar reporte de resultados
pytest


📋 Escenarios de Prueba Cubiertos
Módulo de Autenticación (Login):

Ingreso exitoso con múltiples tipos de usuarios.

Validación de mensajes de error para credenciales incorrectas.

Control de seguridad para usuarios bloqueados (Locked out user).

Validación de campos obligatorios (Usuario y contraseña vacíos).

Módulo de Inventario (En desarrollo):

Verificación de carga dinámica de productos.

Validación de funcionalidad "Add to Cart" y actualización del contador.

📊 Reportabilidad y Evidencias
Al finalizar la ejecución, se genera automáticamente un archivo llamado reporte.html en la raíz del proyecto. Este reporte incluye:

Estado de cada test (Passed/Failed).

Tiempo de ejecución por escenario.

Detalles técnicos en caso de fallos.

Desarrollado por: Abraham - QA Automation Engineer
