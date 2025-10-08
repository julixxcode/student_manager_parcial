from student_manager.repositories import student_repo
from student_manager.config import settings
import json
import tempfile

def test_add_and_get_student(tmp_path, monkeypatch):
    fake_file = tmp_path / "students.json"
    monkeypatch.setattr(settings, "STUDENTS_FILE", fake_file)

    student = {"id": "123", "name": "Julian", "age": 21, "career": "Software", "grades": [4,5,4], "average": 4.3, "status": "Aprobado"}
    student_repo.add_student(student)
    data = student_repo.get_all_students()
    assert len(data) == 1
    assert data[0]["name"] == "Julian"

def test_update_student(tmp_path, monkeypatch):
    fake_file = tmp_path / "students.json"
    monkeypatch.setattr(settings, "STUDENTS_FILE", fake_file)

    s = {"id": "001", "name": "Ana", "age": 20, "career": "Diseño", "grades": [3,3,3], "average": 3.0, "status": "Aprobado"}
    with open(fake_file, "w", encoding="utf-8") as f:
        json.dump([s], f)

    ok = student_repo.update_student("001", {"career": "Arquitectura"})
    assert ok
    data = student_repo.get_all_students()
    assert data[0]["career"] == "Arquitectura"
