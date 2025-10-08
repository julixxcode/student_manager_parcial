from student_manager.services import student_service
from pathlib import Path
import pytest

def test_import_from_csv(tmp_path, monkeypatch):
    """Prueba la importación de estudiantes desde un archivo CSV temporal."""
    fake_file = tmp_path / "students.json"
    monkeypatch.setattr(student_service.settings, "STUDENTS_FILE", fake_file)

    # Crear un CSV temporal simulado
    csv_path = tmp_path / "data.csv"
    csv_content = "Nombre,Edad,Carrera,Nota1,Nota2,Nota3\n"
    csv_content += "Julian,21,Software,4.0,4.5,4.7\n"
    csv_content += "Ana,22,Diseño,3.5,3.6,3.7\n"
    csv_path.write_text(csv_content, encoding="utf-8")

    ok = student_service.import_from_csv(csv_path)
    assert ok is True

    data = student_service.list_students()
    assert len(data) == 2
    assert any(s["name"] == "Julian" for s in data)
    assert any(s["career"] == "Diseño" for s in data)
