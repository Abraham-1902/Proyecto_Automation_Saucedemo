# 🧪 QA Automation Project - SauceDemo

Este repositorio contiene un **framework de automatización de pruebas end-to-end** desarrollado sobre la aplicación web **SauceDemo**, enfocado en validar funcionalidades críticas mediante buenas prácticas de QA.

El proyecto implementa **Python + Playwright** junto con el patrón **Page Object Model (POM)**, garantizando un código **escalable, mantenible y alineado a estándares profesionales**.

---

## 🎯 Objetivo del Proyecto

Validar el correcto funcionamiento de los módulos principales de la aplicación:

- Autenticación de usuarios
- Gestión de inventario
- Interacciones críticas del usuario

**Aplicando:**
- ✔️ Pruebas funcionales
- ✔️ Validaciones negativas (manejo de errores)
- ✔️ Buenas prácticas de automatización

---

## 🏗️ Arquitectura del Framework

El proyecto sigue una estructura modular clara:

```text
📁 Proyecto_Automation_Saucedemo
┣ 📁 pages          # Page Objects (locators + acciones)
┣ 📁 tests          # Casos de prueba
┣ 📁 data           # Datos de prueba (JSON)
┣ 📁 reports        # Resultados de ejecución
┣ 📄 conftest.py    # Configuración global (fixtures)
┣ 📄 pytest.ini     # Configuración del runner
┗ 📄 README.md      # Documentación
🛠️ Stack Tecnológico
Python 3.x

Playwright

Pytest

Pytest-HTML

⚡ Quick Start (Ejecución rápida)
Copia y pega estos comandos en tu terminal para configurar y ejecutar el proyecto:

Bash
# 1. Clonar repositorio
git clone [https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git](https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git)
cd Proyecto_Automation_Saucedemo

# 2. Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\activate

# 3. Instalar dependencias
pip install pytest-playwright pytest-html
playwright install chromium

# 4. Ejecutar pruebas
pytest
🧪 Escenarios de Prueba
🔐 Login
[x] Login exitoso con diferentes usuarios.

[x] Validación de credenciales inválidas.

[x] Usuario bloqueado (locked_out_user).

[x] Validación de campos obligatorios.

🛒 Inventario (En desarrollo)
[x] Verificación de carga de productos.

[ ] Funcionalidad "Add to Cart".

[ ] Validación del contador del carrito.

📊 Reportes y Evidencia
Al ejecutar las pruebas, se genera automáticamente el archivo: reporte.html

El reporte incluye:

Estado de cada test (Pass/Fail).

Tiempo de ejecución.

Detalles técnicos en caso de fallo.

🧠 Buenas Prácticas Implementadas
Page Object Model (POM): Desacoplamiento de la interfaz y la lógica.

Data-Driven Testing: Pruebas basadas en datos externos.

Fixtures: Uso eficiente de recursos con Pytest.

Clean Code: Código legible y mantenible.

👨‍💻 Autor
Abraham QA Automation Engineer
