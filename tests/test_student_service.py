import pytest
from student_manager.services import student_service

@pytest.fixture
def sample_students(tmp_path, monkeypatch):
    """Crea un conjunto temporal de estudiantes para las pruebas."""
    file = tmp_path / "students.json"
    monkeypatch.setattr(student_service.settings, "STUDENTS_FILE", file)
    student_service.create_student("Julian", 21, "Software", [4.0, 3.5, 5.0])
    student_service.create_student("Laura", 19, "Diseño", [2.5, 2.8, 3.0])
    return student_service.list_students()

def test_list_students(sample_students):
    students = sample_students
    assert len(students) == 2

def test_filter_by_career(sample_students):
    results = student_service.filter_students(career="Software")
    assert len(results) == 1
    assert results[0]["career"] == "Software"

def test_filter_by_status(sample_students):
    results = student_service.filter_students(status="Aprobado")
    assert all(s["status"] == "Aprobado" for s in results)

def test_statistics(sample_students):
    stats = student_service.get_statistics()
    assert stats["total"] == 2
    assert "average" in stats
    assert stats["approved"] >= 0

def test_export_to_csv(sample_students):
    path = student_service.export_to_csv()
    assert path.exists()
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Nombre" in content
