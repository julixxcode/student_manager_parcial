"""
Módulo de repositorios.
Maneja la persistencia de datos en formato JSON.
"""

from .student_repo import (
    add_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)
