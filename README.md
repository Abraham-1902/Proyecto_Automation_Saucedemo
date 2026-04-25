![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Playwright](https://img.shields.io/badge/playwright-%232EAD33.svg?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-%230A9EDC.svg?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?sty

# 🚀 SauceDemo End-to-End Automation Framework

Este repositorio alberga un framework de automatización de pruebas de alto impacto para la plataforma **SauceDemo**. Se ha diseñado bajo estándares profesionales, priorizando la **trazabilidad**, la **escalabilidad** y la **visibilidad de resultados**.

## 🛠️ Stack Tecnológico & Patrones
* **Lenguaje:** Python 3.x
* **Motor de Pruebas:** Playwright
* **Test Runner:** Pytest
* **Patrón de Diseño:** Page Object Model (POM)
* **Reportes:** Pytest-HTML / Playwright Trace Viewer

---

## 🗺️ Roadmap de Implementación (Sprints)

Utilizamos una metodología orientada a **Sprints** para garantizar la entrega continua de valor y una cobertura total del sistema.

### 🟢 Sprint 1: Gestión de Acceso & Seguridad (Completado)
*Foco: Validar el flujo de autenticación y el manejo de estados de usuario.*
- [x] **POM:** Implementación de `LoginPage` con selectores optimizados.
- [x] **Test:** Login exitoso con múltiples perfiles (Data-Driven).
- [x] **Test:** Validación de usuario bloqueado (`locked_out_user`).
- [x] **Test:** Control de errores por credenciales inválidas y campos vacíos.
- [x] **Evidencia:** [Ver Reporte y Capturas del Sprint 1](./docs/evidencias/sprint1/)

### 🟡 Sprint 2: Inventario & Experiencia de Usuario (En Desarrollo)
*Foco: Asegurar que el catálogo de productos sea funcional y preciso.*
- [x] **POM:** `InventoryPage` y componentes de productos.
- [x] **Test:** Verificación de carga correcta de imágenes y textos.
- [ ] **Test:** Automatización de filtros de ordenamiento (A-Z, Z-A, Precio).
- [ ] **Test:** Navegación detallada al producto individual.

### ⚪ Sprint 3: E-Commerce Core (Backlog)
*Foco: El corazón del negocio; desde el carrito hasta la confirmación de orden.*
- [ ] Gestión del Carrito (Agregar/Quitar productos).
- [ ] Flujo de Checkout (Información del cliente, impuestos y totales).

### ⚪ Sprint 4: Calidad & CI/CD (Planificado)
*Foco: Robustez técnica y ejecución automatizada.*
- [ ] Implementación de reportes HTML automáticos con capturas en fallos.
- [ ] Configuración de GitHub Actions para integración continua.

---

## 🏗️ Arquitectura del Proyecto
```text
📁 Proyecto_Automation_Saucedemo
┣ 📁 pages          # Page Objects (Encapsulamiento de locators y acciones)
┣ 📁 tests          # Scripts de prueba organizados por módulo/sprint
┣ 📁 data           # Datasets para pruebas parametrizadas
┣ 📁 docs           # Documentación técnica y evidencias de QA
┃ ┗ 📁 evidencias   # Screenshots y reportes HTML por Sprint
┣ 📄 conftest.py    # Fixtures globales y configuración de Playwright
┗ 📄 pytest.ini     # Configuración del runner y parámetros de ejecución

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
