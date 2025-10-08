from student_manager.domain.student import Student

def test_average_calculation():
    """Prueba que el cálculo del promedio sea correcto."""
    s = Student("Julian", 22, "Software", [4.0, 3.5, 5.0])
    assert s.average() == 4.17

def test_status_approved():
    """Prueba que el estudiante sea aprobado si el promedio >= 3.0."""
    s = Student("Maria", 21, "Diseño", [3.0, 3.5])
    assert s.status() == "Aprobado"

def test_status_failed():
    """Prueba que el estudiante sea reprobado si el promedio < 3.0."""
    s = Student("Luis", 23, "Derecho", [2.0, 2.5])
    assert s.status() == "Reprobado"

def test_to_dict_contains_expected_keys():
    """Prueba que el método to_dict tenga las claves esperadas."""
    s = Student("Ana", 20, "Arquitectura", [4.0, 4.5])
    d = s.to_dict()
    for key in ["id", "name", "age", "career", "grades", "average", "status"]:
        assert key in d
