"""
Capa de servicios: define la lógica de negocio
y orquesta el flujo entre domain y repositories.
"""

from student_manager.domain.student import Student
from student_manager.repositories import student_repo

def create_student(name, age, career, grades):
    """Crea un estudiante validado y lo guarda en el archivo JSON."""
    student = Student(name, age, career, grades)
    student_repo.add_student(student.to_dict())
    return student.to_dict()

def list_students():
    """Devuelve la lista completa de estudiantes almacenados."""
    return student_repo.get_all_students()

def find_student(student_id: str):
    """Busca un estudiante por su ID."""
    return student_repo.get_student_by_id(student_id)

def modify_student(student_id, **kwargs):
    """Modifica los datos de un estudiante existente."""
    filtered_data = {k: v for k, v in kwargs.items() if v is not None}
    return student_repo.update_student(student_id, filtered_data)

def remove_student(student_id: str):
    """Elimina un estudiante del archivo JSON."""
    return student_repo.delete_student(student_id)
def filter_students(career: str = None, status: str = None) -> list:
    """
    Filtra estudiantes por carrera o estado académico.
    - career: nombre de la carrera (opcional)
    - status: 'Aprobado' o 'Reprobado' (opcional)
    """
    students = student_repo.get_all_students()

    if career:
        students = [s for s in students if s["career"].lower() == career.lower()]

    if status:
        students = [s for s in students if s["status"].lower() == status.lower()]

    return students


def get_statistics() -> dict:
    """Devuelve estadísticas globales del sistema."""
    students = student_repo.get_all_students()
    if not students:
        return {"total": 0, "average": 0, "approved": 0, "reproved": 0}

    total = len(students)
    avg = round(sum(s["average"] for s in students) / total, 2)
    approved = len([s for s in students if s["status"] == "Aprobado"])
    reproved = total - approved
    return {
        "total": total,
        "average": avg,
        "approved": approved,
        "reproved": reproved
    }
