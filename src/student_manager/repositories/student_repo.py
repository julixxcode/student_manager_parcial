import json
import os
from typing import List, Dict, Optional, Any

# Ruta del archivo JSON donde se guardarán los datos
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "students.json")


def _ensure_file_exists():
    """Crea el archivo JSON si no existe."""
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump([], f)


def load_students() -> List[Dict[str, Any]]:
    """Carga todos los estudiantes desde el archivo JSON."""
    _ensure_file_exists()
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_students(students: List[Dict[str, Any]]):
    """Guarda la lista completa de estudiantes en el archivo JSON."""
    _ensure_file_exists()
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)


def list_all() -> List[Dict[str, Any]]:
    """Devuelve todos los estudiantes."""
    return load_students()


def get_by_id(student_id: str) -> Optional[Dict[str, Any]]:
    """Busca un estudiante por su ID."""
    for student in load_students():
        if student["id"] == student_id:
            return student
    return None


def add(student: Dict[str, Any]) -> Dict[str, Any]:
    """Agrega un nuevo estudiante al archivo."""
    students = load_students()
    students.append(student)
    save_students(students)
    return student


def delete(student_id: str) -> bool:
    """Elimina un estudiante por ID. Devuelve True si se eliminó."""
    students = load_students()
    new_students = [s for s in students if s["id"] != student_id]
    if len(new_students) != len(students):
        save_students(new_students)
        return True
    return False


def update(student_id: str, **changes) -> bool:
    """Actualiza los datos de un estudiante."""
    students = load_students()
    updated = False
    for s in students:
        if s["id"] == student_id:
            s.update(changes)
            updated = True
            break
    if updated:
        save_students(students)
    return updated
