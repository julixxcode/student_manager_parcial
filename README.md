# 🧮 Student Manager System

Sistema modular de gestión de estudiantes desarrollado en **Python 3.12**, con un enfoque en **análisis académico, generación de rankings, gestión de historiales y exportación de datos**.  
Incluye un conjunto completo de **tests unitarios e integrados**, logrando un código altamente confiable y mantenible.

---

## 📚 Descripción general

`student_manager` es una aplicación diseñada para procesar información académica de estudiantes, calcular promedios, generar rankings globales y por carrera, filtrar rendimientos y exportar resultados en diferentes formatos.  
El sistema está organizado bajo una arquitectura modular con **pruebas automáticas**, **flujo Git profesional** y **estructura escalable para futuras integraciones** (CLI, API REST, o dashboards).

---

## 🏗️ Arquitectura del proyecto

parcial_hely/
│
├── src/
│ └── student_manager/
│ ├── analytics/ # Módulos de análisis existentes
│ ├── cli/ # CLI (interfaz de comandos)
│ ├── config/ # Configuración general
│ ├── domain/ # Entidades y modelos
│ ├── repositories/ # Repositorios de datos
│ ├── reports/ # Reportes y estadísticas
│ ├── services/ # Lógica de negocio principal
│ ├── utils/ # Funciones auxiliares
│ │
│ ├── ranking.py # ✅ Ranking global y por carrera
│ ├── history.py # ✅ Historial académico individual
│ ├── exporter.py # ✅ Exportación de datos a CSV/JSON
│ ├── filters.py # ✅ Filtros y agrupación por rendimiento
│ └── init.py
│
└── tests/
├── unit/ # ✅ Pruebas unitarias
│ ├── test_ranking.py
│ ├── test_history.py
│ ├── test_exporter.py
│ └── test_filters.py
│
└── integration/ # ✅ Pruebas de integración (flujo completo)
└── test_full_flow.py

yaml
Copiar código

---

## ⚙️ Instalación y entorno de desarrollo

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/usuario/parcial_hely.git
   cd parcial_hely
Crear y activar entorno virtual

bash
Copiar código
python -m venv .venv
.venv\Scripts\activate
Instalar dependencias

bash
Copiar código
pip install -r requirements.txt
🧠 Funcionalidades principales
1. 🏆 ranking.py
Calcula el ranking global de los estudiantes, o por carrera, en base a las notas disponibles.

Funciones:

rank_students_global(students, min_courses=1, top=None)

rank_students_by_career(students)

Ejemplo de uso:

python
Copiar código
from student_manager.ranking import rank_students_global

students = [
    {"id": 1, "name": "Ana", "career": "Sistemas", "grades": [4.5, 4.7]},
    {"id": 2, "name": "Bruno", "career": "Civil", "grades": [3.2, 3.5]},
]
ranking = rank_students_global(students)
2. 🧾 history.py
Gestiona y resume el historial académico individual de cada estudiante.

Funciones:

get_history(student)

history_summary(student)

Ejemplo:

python
Copiar código
from student_manager.history import history_summary

student = {"id": 1, "name": "Ana", "grades": [4.0, 4.5, 4.8]}
summary = history_summary(student)
3. 💾 exporter.py
Permite exportar los resultados generados por los rankings o filtros a archivos CSV o JSON.

Funciones:

export_to_csv(students, filename)

export_to_json(students, filename)

Ejemplo:

python
Copiar código
from student_manager.exporter import export_to_json
export_to_json(students, "ranking.json")
4. 📊 filters.py
Proporciona filtros de rendimiento y agrupaciones estadísticas según los promedios obtenidos.

Funciones:

filter_by_average(students, min_avg=None, max_avg=None)

group_by_ranges(students, ranges)

Ejemplo:

python
Copiar código
from student_manager.filters import filter_by_average
filter_by_average(students, min_avg=4.0)
🧪 Testing y cobertura
El proyecto incluye una cobertura amplia con Pytest, abarcando tanto pruebas unitarias como de integración.

Ejecutar pruebas:
bash
Copiar código
pytest -q
Ejecutar con reporte de cobertura:
bash
Copiar código
pytest --cov=student_manager --cov-report=term-missing
Generar reporte HTML:
bash
Copiar código
pytest --cov=student_manager --cov-report=html
Abrir en navegador:

bash
Copiar código
htmlcov/index.html
Cobertura actual: ~98–100%

🧱 Estándares y buenas prácticas
Convención de commits: Conventional Commits (feat:, fix:, test:, refactor:).

Testing framework: pytest con fixtures tmp_path y monkeypatch.

Estilo: PEP8 y tipado con mypy compatible.

Arquitectura: separación por dominio (services, repositories, reports, cli).

Documentación: README y docstrings descriptivos en cada módulo.

🚀 Flujo de desarrollo con Git
bash
Copiar código
# Crear una rama para nuevas funcionalidades
git checkout -b feature/nueva-funcionalidad

# Agregar cambios
git add .

# Commit siguiendo convención
git commit -m "feat: descripción clara del cambio"

# Subir a remoto
git push origin feature/nueva-funcionalidad

# Crear Pull Request hacia main
🧩 Próximas mejoras planificadas
 Dashboard CLI interactivo (student_manager/cli/dashboard.py)
para ejecutar rankings, filtros y exportaciones desde la terminal.

 Integración futura con FastAPI o Flask.

 Configurar GitHub Actions para pruebas automáticas.

 Publicar documentación técnica en docs/.

👨‍💻 Autor
Julian Murcia
Estudiante de Ingeniería de Software – FESC
Proyecto académico: Codificación y Pruebas de Software
📍 Cúcuta, Norte de Santander – Colombia

GitHub: @julianmurcia

