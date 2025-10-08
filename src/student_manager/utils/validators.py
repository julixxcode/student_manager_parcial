"""
Validadores de datos para Student Manager.
Garantizan que los valores de entrada sean correctos antes de crear o actualizar estudiantes.
"""

from student_manager.config import settings

def validate_name(name: str) -> bool:
    """Valida que el nombre sea una cadena no vacía de al menos 2 caracteres."""
    return isinstance(name, str) and len(name.strip()) >= 2

def validate_age(age: int) -> bool:
    """Valida que la edad esté dentro del rango permitido (10 a 100 años)."""
    return isinstance(age, int) and 10 <= age <= 100

def validate_grades(grades: list[float]) -> bool:
    """Valida que las notas estén entre los valores mínimos y máximos definidos."""
    if not isinstance(grades, list) or not grades:
        return False
    return all(settings.MIN_GRADE <= g <= settings.MAX_GRADE for g in grades)
