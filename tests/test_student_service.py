from student_manager.services import student_service as svc
import os

def setup_module(module):
    """Antes de correr las pruebas, limpia el archivo JSON."""
    data_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "students.json"
    )
    if os.path.exists(data_path):
        os.remove(data_path)

def test_create_and_find_student():
    """Prueba la creación y búsqueda de un estudiante."""
    student = svc.create_student("Camilo", 20, "Ingeniería", [4.0, 4.5])
    found = svc.find_student(student["id"])

    assert found is not None
    assert found["name"] == "Camilo"
    assert found["status"] == "Aprobado"

def test_modify_student():
    """Prueba la actualización de datos."""
    student = svc.create_student("Andres", 22, "Diseño", [2.5, 3.0])
    svc.modify_student(student["id"], grades=[4.0, 5.0])
    updated = svc.find_student(student["id"])

    assert updated["average"] >= 3.0
    assert updated["status"] == "Aprobado"

def test_remove_student():
    """Prueba la eliminación de un estudiante."""
    student = svc.create_student("Laura", 25, "Contaduría", [3.0, 3.5])
    result = svc.remove_student(student["id"])
    assert result is True
