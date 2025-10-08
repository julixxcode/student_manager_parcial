"""
Módulo de acceso a datos.
Gestiona la persistencia de estudiantes en formato JSON.
Incluye creación de respaldos automáticos.
"""

import json
from datetime import datetime
from student_manager.config import settings

# ============================================================
# 🔹 FUNCIONES INTERNAS (NO PÚBLICAS)
# ============================================================

def _load_data() -> list:
    """Carga los datos desde el archivo JSON."""
    try:
        with open(settings.STUDENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def _save_data(data: list):
    """Guarda la lista de estudiantes en el archivo principal."""
    with open(settings.STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    _backup_data(data)  # 🔁 respaldo automático


def _backup_data(data: list):
    """Crea un respaldo automático de los datos."""
    backup_path = settings.DATA_DIR / "students_backup.json"
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# ============================================================
# 🔹 OPERACIONES CRUD
# ============================================================

def get_all_students() -> list:
    """Devuelve todos los estudiantes."""
    return _load_data()


def get_student_by_id(student_id: str) -> dict | None:
    """Busca un estudiante por su ID."""
    for s in _load_data():
        if s["id"] == student_id:
            return s
    return None


def add_student(student: dict):
    """Agrega un nuevo estudiante y guarda los cambios."""
    data = _load_data()
    data.append(student)
    _save_data(data)


def update_student(student_id: str, updated: dict) -> bool:
    """Actualiza un estudiante existente."""
    data = _load_data()
    for i, s in enumerate(data):
        if s["id"] == student_id:
            updated["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data[i].update(updated)
            _save_data(data)
            return True
    return False


def delete_student(student_id: str) -> bool:
    """Elimina un estudiante por su ID."""
    data = _load_data()
    new_data = [s for s in data if s["id"] != student_id]
    if len(new_data) == len(data):
        return False
    _save_data(new_data)
    return True
