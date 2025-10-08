"""
Configuración global del sistema Student Manager.
Centraliza rutas, constantes y parámetros de control.
"""

import os
from pathlib import Path

# Raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Carpeta de datos y archivo JSON
DATA_DIR = BASE_DIR / "data"
STUDENTS_FILE = DATA_DIR / "students.json"

# Asegurar existencia del directorio
os.makedirs(DATA_DIR, exist_ok=True)

# Constantes del sistema
MIN_GRADE = 0.0
MAX_GRADE = 5.0
PASSING_GRADE = 3.0

# Configuración visual (Rich)
TABLE_STYLES = {
    "title": "bold cyan",
    "header": "bold yellow",
}
