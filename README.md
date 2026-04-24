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
┗ 📄 README.md      # Documentaciónno

```

---


# 🛠️ Stack Tecnológico

```text
Python 3.x
Playwright
Pytest
Pytest-HTML
```

---

## 🧪 Escenarios de Prueba

### 🔐 Login

- [x] 🟢 Login exitoso con diferentes usuarios  
- [x] 🟢 Validación de credenciales inválidas  
- [x] 🟢 Usuario bloqueado (`locked_out_user`)  
- [x] 🟢 Validación de campos obligatorios  

### 🛒 Inventario (En desarrollo)

- [x] 🟡Verificación de carga de productos  
- [ ] 🟡Funcionalidad **Add to Cart**  
- [ ] 🟡Validación del contador del carrito  

---

## 🧠 Buenas Prácticas Implementadas

- **Page Object Model (POM):** Desacoplamiento de la interfaz y la lógica  
- **Data-Driven Testing:** Pruebas basadas en datos externos  
- **Fixtures:** Uso eficiente de recursos con Pytest  
- **Clean Code:** Código legible y mantenible  

---

## 👨‍💻 Autor

**Abraham - QA Automation Engineer**
