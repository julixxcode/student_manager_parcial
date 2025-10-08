from typing import List, Optional, Dict, Any
from student_manager.domain.student import Student
from student_manager.repositories import student_repo as repo


def create_student(name: str, age: int, career: str, grades: List[float]) -> Dict[str, Any]:
    """Crea un nuevo estudiante y lo guarda en el repositorio."""
    student = Student(name=name, age=age, career=career, grades=grades)
    return repo.add(student.to_dict())


def list_students() -> List[Dict[str, Any]]:
    """Devuelve todos los estudiantes registrados."""
    return repo.list_all()


def find_student(student_id: str) -> Optional[Dict[str, Any]]:
    """Busca un estudiante por ID."""
    return repo.get_by_id(student_id)


def remove_student(student_id: str) -> bool:
    """Elimina un estudiante por ID."""
    return repo.delete(student_id)


def modify_student(
    student_id: str,
    name: Optional[str] = None,
    age: Optional[int] = None,
    career: Optional[str] = None,
    grades: Optional[List[float]] = None,
) -> bool:
    """Actualiza los datos de un estudiante."""
    student = repo.get_by_id(student_id)
    if not student:
        return False

    changes: Dict[str, Any] = {}
    if name is not None:
        changes["name"] = name
    if age is not None:
        changes["age"] = age
    if career is not None:
        changes["career"] = career
    if grades is not None:
        # Recalcular promedio y estado si cambian las notas
        new_student = Student(
            name=student["name"],
            age=student["age"],
            career=student["career"],
            grades=grades,
            id=student["id"],
        )
        changes["grades"] = grades
        changes["average"] = new_student.average()
        changes["status"] = new_student.status()

    return repo.update(student_id, **changes)
