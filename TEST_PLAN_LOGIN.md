# Plan de Pruebas: Módulo de Autenticación (Sprint 1)

## 1. Información General
* **Proyecto:** Automatización SauceDemo
* **Sprint:** 1
* **Módulo:** Login / Seguridad
* **Responsable:** Abraham (QA Automation)

## 2. Estrategia de Automatización
Se utiliza un enfoque **Data-Driven Testing** bajo el patrón de diseño **Page Object Model (POM)**. Los datos de prueba se gestionan de forma externa en archivos JSON para facilitar el mantenimiento.

## 3. Matriz de Trazabilidad de Casos de Prueba
## 3. Matriz de Trazabilidad
|       ID  |       Escenario    | Tipo | Resultado Esperado |
| **TC001** | Login Exitoso      | (+)  | Acceso a /inventory.html |
| **TC002** | Usuario Incorrecto | (-)  | Error: Credentials mismatch |
| **TC003** | Clave Incorrecta   | (-)  | Error: Credentials mismatch |
| **TC004** | Usuario Vacío      | (-)  | Error: Username required |
| **TC005** | Clave Vacía        | (-)  | Error: Password required |
| **TC006** | Ambos Vacíos       | (-)  | Error: Username required |
| **TC007** | Usuario Bloqueado  | (-)  | Error: User locked out |

## 4. Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Framework:** Playwright (pytest-playwright)
* **Motor de Pruebas:** Pytest
* **Formato de Datos:** JSON

## 5. Ejecución
Para ejecutar este plan de pruebas:
```bash
pytest -v --headed