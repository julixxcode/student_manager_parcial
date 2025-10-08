from student_manager.domain.student import Student
import pytest

def test_create_valid_student():
    s = Student("Julian", 21, "Software", [4.0, 3.5, 5.0])
    assert s.name == "Julian"
    assert s.career == "Software"
    assert s.average() == 4.17
    assert s.status() == "Aprobado"

def test_invalid_name():
    with pytest.raises(ValueError):
        Student("", 20, "Software", [3.0, 3.5])

def test_invalid_age():
    with pytest.raises(ValueError):
        Student("Ana", 5, "Software", [3.0])

def test_invalid_grades():
    with pytest.raises(ValueError):
        Student("Carlos", 25, "Software", [10])

def test_str_representation():
    s = Student("Laura", 23, "Sistemas", [4.5, 4.0, 4.8])
    assert "Laura" in str(s)
    assert "Sistemas" in str(s)
