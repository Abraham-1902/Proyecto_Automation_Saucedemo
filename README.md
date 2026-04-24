# 🧪 QA Automation Project - SauceDemo

Este repositorio contiene un **framework de automatización de pruebas end-to-end** desarrollado sobre la aplicación web **SauceDemo**, enfocado en validar funcionalidades críticas mediante buenas prácticas de QA.

El proyecto implementa **Python + Playwright** junto con el patrón **Page Object Model (POM)**, garantizando un código **escalable, mantenible y alineado a estándares profesionales**.

---

## 🎯 Objetivo del Proyecto

Validar el correcto funcionamiento de los módulos principales de la aplicación:

- Autenticación de usuarios
- Gestión de inventario
- Interacciones críticas del usuario

Aplicando:
- ✔️ Pruebas funcionales  
- ✔️ Validaciones negativas (manejo de errores)  
- ✔️ Buenas prácticas de automatización  

---

## 🏗️ Arquitectura del Framework

El proyecto sigue una estructura modular clara:


📁 Proyecto_Automation_Saucedemo
┣ 📁 pages → Page Objects (locators + acciones)
┣ 📁 tests → Casos de prueba
┣ 📁 data → Datos de prueba (JSON)
┣ 📁 reports → Resultados de ejecución
┣ 📄 conftest.py → Configuración global (fixtures)
┣ 📄 pytest.ini → Configuración del runner
┣ 📄 README.md


---

## 🛠️ Stack Tecnológico

- **Python 3.x**
- **Playwright**
- **Pytest**
- **Pytest-HTML**

---

## ⚡ Quick Start (Ejecución rápida)

### 1. Clonar repositorio
```bash
git clone https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git
cd Proyecto_Automation_Saucedemo
2. Crear entorno virtual
python -m venv venv
.\venv\Scripts\activate
3. Instalar dependencias
pip install pytest-playwright pytest-html
playwright install
4. Ejecutar pruebas
pytest
🧪 Escenarios de Prueba
🔐 Login
Login exitoso con diferentes usuarios
Validación de credenciales inválidas
Usuario bloqueado (locked_out_user)
Validación de campos obligatorios
🛒 Inventario (En desarrollo)
Verificación de carga de productos
Funcionalidad "Add to Cart"
Validación del contador del carrito
📊 Reportes y Evidencia

Al ejecutar las pruebas se genera automáticamente:

📄 reporte.html

Incluye:

Estado de cada test (Pass/Fail)
Tiempo de ejecución
Detalles técnicos en caso de fallo
🧠 Buenas Prácticas Implementadas
Page Object Model (POM)
Data-Driven Testing
Uso de fixtures con Pytest
Separación de responsabilidades
Código limpio y mantenible
👨‍💻 Autor

Abraham
QA Automation Engineer
