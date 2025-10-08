"""
Gestión de datos persistentes de estudiantes en formato JSON.
Se encarga de guardar, leer, actualizar y eliminar registros.
"""

import json
import os
from student_manager.config import settings

def _load_data() -> list:
    """Carga los datos desde el archivo JSON. Si no existe, devuelve una lista vacía."""
    if not os.path.exists(settings.STUDENTS_FILE):
        return []
    with open(settings.STUDENTS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def _save_data(data: list):
    """Guarda la lista de estudiantes en el archivo JSON."""
    with open(settings.STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_all_students() -> list:
    """Devuelve la lista completa de estudiantes almacenados."""
    return _load_data()

def get_student_by_id(student_id: str):
    """Busca un estudiante por su ID."""
    return next((s for s in _load_data() if s["id"] == student_id), None)

def add_student(student: dict):
    """Agrega un nuevo estudiante al archivo JSON."""
    data = _load_data()
    data.append(student)
    _save_data(data)

def update_student(student_id: str, updated: dict) -> bool:
    """Actualiza los datos de un estudiante existente."""
    data = _load_data()
    for i, s in enumerate(data):
        if s["id"] == student_id:
            data[i].update(updated)
            _save_data(data)
            return True
    return False

def delete_student(student_id: str) -> bool:
    """Elimina un estudiante del archivo JSON."""
    data = _load_data()
    new_data = [s for s in data if s["id"] != student_id]
    if len(new_data) == len(data):
        return False
    _save_data(new_data)
    return True
