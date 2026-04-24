# 🧪 Proyecto de Automatización: SauceDemo

Este repositorio contiene un framework de pruebas automatizadas profesional para la plataforma **SauceDemo**. El proyecto está desarrollado en **Python** utilizando **Playwright**, aplicando el patrón de diseño **Page Object Model (POM)** para garantizar un código limpio, mantenible y escalable.

---

## 🏗️ Arquitectura del Proyecto
El framework separa la lógica de negocio de la lógica de los tests para facilitar el mantenimiento:

* **`pages/`**: Contiene las clases de las páginas (Locators y Acciones).
* **`tests/`**: Scripts de prueba que ejecutan los escenarios de validación.
* **`data/`**: Gestión de datos de prueba mediante archivos JSON (Data-Driven).
* **`pytest.ini`**: Configuración centralizada del runner (Headless, SlowMo, Reportes).

---

## 🛠️ Stack Tecnológico
| Herramienta | Uso |
| :--- | :--- |
| **Python** | Lenguaje de programación principal. |
| **Playwright** | Motor de automatización para interacciones web. |
| **Pytest** | Framework de pruebas para orquestar la ejecución. |
| **Pytest-HTML** | Generador de reportes visuales de ejecución. |

---

## 🚀 Configuración y Ejecución Técnica

### 1. Preparación del Entorno
Clona el proyecto y configura el entorno virtual:
```bash
git clone [https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git](https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git)
cd Proyecto_Automation_Saucedemo
python -m venv venv
.\venv\Scripts\activate  # En Windows
