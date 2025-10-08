"""
Capa de servicios del sistema Student Manager.
Coordina la lógica de negocio entre dominio y repositorio.
Incluye filtros, estadísticas, exportación CSV y validaciones.
"""

import csv
from pathlib import Path
from student_manager.domain.student import Student
from student_manager.repositories import student_repo
from student_manager.config import settings

# ============================================================
# 🔹 CREAR ESTUDIANTE
# ============================================================
def create_student(name: str, age: int, career: str, grades: list[float]) -> dict:
    """Crea un nuevo estudiante y lo guarda."""
    student = Student(name, age, career, grades)
    student_repo.add_student(student.to_dict())
    return student.to_dict()

# ============================================================
# 🔹 LISTAR Y BUSCAR
# ============================================================
def list_students() -> list:
    """Devuelve todos los estudiantes registrados."""
    return student_repo.get_all_students()


def find_student(student_id: str) -> dict | None:
    """Busca un estudiante por su ID."""
    return student_repo.get_student_by_id(student_id)

# ============================================================
# 🔹 MODIFICAR Y ELIMINAR
# ============================================================
def modify_student(student_id: str, name=None, age=None, career=None) -> bool:
    """Modifica los datos básicos del estudiante."""
    student = find_student(student_id)
    if not student:
        return False

    updated = {}
    if name:
        updated["name"] = name.title()
    if age:
        updated["age"] = int(age)
    if career:
        updated["career"] = career.title()

    return student_repo.update_student(student_id, updated)


def remove_student(student_id: str) -> bool:
    """Elimina un estudiante por su ID."""
    return student_repo.delete_student(student_id)

# ============================================================
# 🔹 FILTRO Y ESTADÍSTICAS
# ============================================================
def filter_students(career: str = None, status: str = None) -> list:
    """
    Filtra estudiantes por carrera o estado académico.
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

# ============================================================
# 🔹 EXPORTAR DATOS A CSV
# ============================================================
def export_to_csv():
    """
    Exporta todos los estudiantes a un archivo CSV en la carpeta /data.
    Retorna la ruta del archivo exportado.
    """
    students = student_repo.get_all_students()
    if not students:
        raise ValueError("No hay estudiantes para exportar.")

    csv_path = settings.DATA_DIR / "students_export.csv"

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Nombre", "Edad", "Carrera", "Promedio", "Estado", "Creado", "Actualizado"])
        for s in students:
            writer.writerow([
                s["id"], s["name"], s["age"], s["career"],
                s["average"], s["status"],
                s.get("created_at", ""), s.get("updated_at", "")
            ])

    return csv_path
