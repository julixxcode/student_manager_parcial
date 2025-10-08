# 📘 Student Manager – Proyecto de Pruebas en Python

Proyecto desarrollado como parte del **Parcial de Codificación y Pruebas de Software (FESC)**.  
Implementa un sistema de gestión de estudiantes con registro, actualización, eliminación y cálculo automático de promedios.

---

## 🧠 Objetivo
Aplicar conceptos de **arquitectura modular, programación estructurada y pruebas unitarias**, usando:
- **Python 3.11+**
- **Typer** y **Rich** para la interfaz de comandos (CLI)
- **pytest** para pruebas automatizadas
- **JSON** como sistema de persistencia de datos

---

## 🧱 Estructura del Proyecto

parcial_hely/
├─ data/ → Almacena el archivo students.json
├─ src/
│ └─ student_manager/
│ ├─ domain/ → Modelo Student (lógica de promedio y estado)
│ ├─ repositories/ → Funciones de lectura/escritura JSON
│ ├─ services/ → Lógica de negocio (CRUD)
│ └─ cli/ → Interfaz de línea de comandos (Typer + Rich)
└─ tests/ → Pruebas automáticas (pytest)


---

## ⚙️ Instalación

```bash
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar entorno (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -e .
pip install typer rich pytest pytest-cov

🚀 Uso del sistema

Agregar un estudiante:

python -m student_manager.cli.app add


Listar estudiantes:

python -m student_manager.cli.app list


Buscar un estudiante por ID:

python -m student_manager.cli.app get <id>


Eliminar un estudiante:

python -m student_manager.cli.app delete <id>


Actualizar datos:

python -m student_manager.cli.app update <id> --name "Nuevo Nombre" --age 25

🧪 Pruebas Unitarias

Ejecutar pruebas:

pytest -v


Generar reporte de cobertura:

pytest --cov=student_manager --cov-report=term-missing

✨ Autor

Julian Murcia
FESC – Ingeniería de Software
Cúcuta, Norte de Santander