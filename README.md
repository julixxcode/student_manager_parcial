# 📘 Student Manager – Sistema Modular de Gestión de Estudiantes en Python

Proyecto desarrollado como parte del **Parcial de Codificación y Pruebas de Software (FESC)**.  
Su propósito es demostrar el uso de **arquitectura modular, pruebas automatizadas y contenedores Docker** para la gestión de información académica.

---

## 🧠 Objetivo General
Aplicar conceptos de:
- **Arquitectura modular (Domain, Repositories, Services, Analytics, CLI)**
- **Pruebas estructuradas y unitarias con pytest**
- **Dockerización del entorno de ejecución**
- **Procesamiento de datos JSON y CSV**
- **Creación de interfaces CLI interactivas con Typer y Rich**

---

## 🧱 Estructura del Proyecto

parcial_hely/
├── data/
│ ├── students.json # Persistencia principal
│ ├── students.csv # Importación de datos CSV
│
├── src/
│ └── student_manager/
│ ├── domain/ # Modelo y lógica del estudiante
│ ├── repositories/ # Módulos de lectura/escritura (JSON y CSV)
│ ├── services/ # Operaciones CRUD
│ ├── utils/ # Funciones auxiliares (promedios, validaciones)
│ ├── analytics/ # NUEVO: Rankings y análisis por carrera
│ │ ├── rankings.py
│ │ ├── rankings_cli.py
│ │ └── init.py
│ └── cli/ # Interfaz de línea de comandos (Typer + Rich)
│
├── tests/ # Pruebas automatizadas (pytest)
│ ├── test_student.py
│ ├── test_analytics.py
│ ├── test_import_csv.py
│ └── ...
│
├── Dockerfile # Imagen para ejecución en contenedor
├── docker-compose.yml # Orquestación local
├── requirements.txt
└── README.md

yaml
Copiar código

---

## ⚙️ Instalación y Configuración del Entorno

### 🧩 1. Crear entorno virtual

```bash
python -m venv .venv
⚡ 2. Activar entorno (Windows PowerShell)
bash
Copiar código
.\.venv\Scripts\Activate.ps1
📦 3. Instalar dependencias necesarias
bash
Copiar código
pip install -e .
pip install typer rich pytest pytest-cov
🚀 Uso del Sistema (CLI Principal)
Ejecutar la interfaz principal basada en Typer:

bash
Copiar código
python -m student_manager.cli.app
Comandos principales
Comando	Descripción
add	Agregar un nuevo estudiante
list	Listar todos los estudiantes
get <id>	Consultar información por ID
update <id> --name "Nuevo Nombre"	Actualizar datos de un estudiante
delete <id>	Eliminar un estudiante

📊 Módulo Analytics (Rankings y Promedios)
El módulo analytics permite realizar análisis y generar reportes de rendimiento académico por carrera.

📘 Uso desde Python
python
Copiar código
from student_manager.analytics import get_average_by_career, get_top_students

students = [
    {"name": "Ana", "career": "Sistemas", "scores": [4.5, 4.2, 4.8]},
    {"name": "Luis", "career": "Sistemas", "scores": [3.9, 4.0, 4.1]},
    {"name": "María", "career": "Industrial", "scores": [4.7, 4.6, 4.8]},
]

print(get_average_by_career(students))
print(get_top_students(students, n=3))
Salida esperada:

bash
Copiar código
{'Sistemas': 4.20, 'Industrial': 4.70}
[{'name': 'María', 'career': 'Industrial', 'average': 4.7},
 {'name': 'Ana', 'career': 'Sistemas', 'average': 4.5},
 {'name': 'Luis', 'career': 'Sistemas', 'average': 4.0}]
💻 Uso del CLI de Analytics
Ejecutar desde terminal:

bash
Copiar código
python -m src.student_manager.analytics.rankings_cli by-career
python -m src.student_manager.analytics.rankings_cli top -n 5
Opciones disponibles:

Opción	Descripción
by-career	Muestra el promedio de cada carrera
top	Muestra el ranking de los mejores estudiantes
--career	Filtra por carrera específica
--json	Exporta resultados en formato JSON

📥 Importación de Datos CSV
El módulo repositories/import_csv.py permite importar estudiantes desde archivos CSV estándar:

python
Copiar código
from student_manager.repositories.import_csv import import_from_csv

students = import_from_csv("data/students.csv")
Cada fila se convierte automáticamente en una estructura estándar reconocida por el sistema y los módulos de análisis.

🧪 Pruebas Automatizadas y Cobertura
Ejecutar todas las pruebas
bash
Copiar código
pytest -v
Generar reporte de cobertura en terminal
bash
Copiar código
pytest --cov=student_manager --cov-report=term-missing
Reporte HTML detallado
bash
Copiar código
pytest --cov=student_manager --cov-report=html
📁 El reporte se genera en:
htmlcov/index.html

🐳 Dockerización del Proyecto
🧰 Construir imagen Docker
bash
Copiar código
docker build -t student-manager .
🚀 Ejecutar contenedor
bash
Copiar código
docker run -it --rm student-manager
🧩 Orquestación con Docker Compose
bash
Copiar código
docker compose up --build
🧾 Tecnologías Implementadas
Tecnología	Propósito
Python 3.11+	Lenguaje principal del proyecto
Typer + Rich	Construcción del CLI interactivo
Pytest + pytest-cov	Pruebas unitarias y cobertura
Docker	Empaquetado y despliegue del entorno
JSON / CSV	Persistencia y carga de datos
Dataclasses	Definición de entidades
Modularización	División lógica por capas funcionales

✨ Autor
👨‍💻 Julian Murcia
Estudiante de Ingeniería de Software – FESC
Cúcuta, Norte de Santander, Colombia
