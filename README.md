# 🧪 Proyecto de Automatización: SauceDemo

Este repositorio contiene un framework de pruebas automatizadas profesional desarrollado para la plataforma **SauceDemo**. El proyecto utiliza **Python** y **Playwright**, aplicando el patrón de diseño **Page Object Model (POM)** para garantizar un código limpio, mantenible y escalable.

---

## 🏗️ Arquitectura del Proyecto
El framework está organizado para separar la lógica de los elementos de la interfaz de la lógica de las pruebas:
* **pages/**: Contiene las clases de las páginas (Locators y Acciones).
* **tests/**: Scripts de prueba que ejecutan los escenarios de validación.
* **data/**: Gestión de datos de prueba mediante archivos JSON (Data-Driven Testing).
* **pytest.ini**: Configuración centralizada del runner (Modo visible, SlowMo y Reportes).
* **conftest.py**: Configuración de fixtures globales para la inicialización del navegador.

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

Para poner en marcha el proyecto, ejecuta los siguientes comandos en tu terminal:

```bash
# Clonar repositorio, configurar entorno e instalar dependencias
git clone [https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git](https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git)
cd Proyecto_Automation_Saucedemo
python -m venv venv
.\venv\Scripts\activate
pip install pytest-playwright pytest-html
playwright install chromium

# Ejecutar las pruebas
pytest
