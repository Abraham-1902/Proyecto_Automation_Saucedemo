![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Playwright](https://img.shields.io/badge/playwright-%232EAD33.svg?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-%230A9EDC.svg?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

# 🚀 SauceDemo End-to-End Automation Framework

Framework de automatización E2E desarrollado sobre **SauceDemo**, diseñado para validar flujos críticos de negocio con un enfoque en **calidad, mantenibilidad y ejecución automatizada**.

---

## 🎯 Objetivo

Validar de forma confiable los principales flujos de la aplicación:

- 🔐 Autenticación de usuarios  
- 🛒 Gestión de inventario  
- 💳 Flujo de compra (en progreso)  

Aplicando:

- ✔️ Pruebas funcionales  
- ✔️ Escenarios negativos  
- ✔️ Data-Driven Testing  
- ✔️ Buenas prácticas de automatización  

---

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.x  
- **Automatización:** Playwright  
- **Test Runner:** Pytest  
- **Patrón:** Page Object Model (POM)  
- **Reportes:** Pytest-HTML + Playwright Trace  

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

## ⚡ Ejecución rápida

git clone https://github.com/Abraham-1902/Proyecto_Automation_Saucedemo.git
cd Proyecto_Automation_Saucedemo

python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install pytest-playwright pytest-html
playwright install chromium

pytest

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

- **Page Object Model (POM):** separación de lógica y UI  
- **Data-Driven Testing:** parametrización con datos externos  
- **Fixtures (Pytest):** reutilización y eficiencia  
- **Clean Code:** legibilidad y mantenibilidad  

---

## 👨‍💻 Autor

**Abraham - QA Automation Engineer**
