import pytest
from student_manager.services import student_service
from pathlib import Path

@pytest.fixture
def sample_data(tmp_path, monkeypatch):
    """Crea un conjunto temporal de estudiantes para pruebas de ranking y promedio por carrera."""
    fake_file = tmp_path / "students.json"
    monkeypatch.setattr(student_service.settings, "STUDENTS_FILE", fake_file)

    student_service.create_student("Julian", 21, "Software", [4.5, 4.7, 4.8])
    student_service.create_student("Laura", 20, "Diseño", [3.0, 3.5, 3.8])
    student_service.create_student("Carlos", 22, "Software", [4.0, 4.3, 4.5])
    student_service.create_student("Maria", 23, "Arquitectura", [3.5, 3.6, 3.7])

    return student_service.list_students()


def test_get_top_students(sample_data):
    """Verifica que el ranking devuelva los estudiantes con mayor promedio."""
    top = student_service.get_top_students(limit=3)
    assert len(top) == 3
    assert top[0]["average"] >= top[1]["average"]


def test_get_average_by_career(sample_data):
    """Verifica el cálculo del promedio general agrupado por carrera."""
    result = student_service.get_average_by_career()
    assert isinstance(result, dict)
    assert "Software" in result
    assert result["Software"] > 4.0
    assert all(isinstance(v, float) for v in result.values())
