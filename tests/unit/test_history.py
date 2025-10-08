from types import SimpleNamespace
from student_manager.history import get_history, history_summary

def test_history_from_list():
    s = SimpleNamespace(id=1, name="Ana", grades=[4.0, 4.5, 3.8])
    h = get_history(s)
    assert len(h) == 3
    assert h[0].term == "T1"

def test_history_summary_stats():
    s = SimpleNamespace(id=2, name="Bruno", history=[
        {"term": "2024-1", "course": "Matemáticas", "grade": 3.5},
        {"term": "2024-2", "course": "Física", "grade": 4.0}
    ])
    summary = history_summary(s)
    assert summary["average"] == 3.75
def test_history_empty_student():
    s = SimpleNamespace(id=3, name="Vacío", grades=[])
    result = history_summary(s)
    assert result["count"] == 0
    assert result["average"] == 0

def test_history_invalid_grade_type():
    s = SimpleNamespace(id=4, name="Erróneo", history=[{"term": "T1", "course": "Test", "grade": "no-numero"}])
    # Debe lanzar ValueError o convertir a float sin error
    try:
        summary = history_summary(s)
        assert "average" in summary
    except Exception as e:
        assert isinstance(e, (ValueError, TypeError))
