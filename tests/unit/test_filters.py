from types import SimpleNamespace
from student_manager.filters import filter_by_average, group_by_ranges

def s():
    return [
        SimpleNamespace(id=1, name="Ana", career="Sistemas", grades=[4.5, 4.0]),
        SimpleNamespace(id=2, name="Bruno", career="Civil", grades=[3.2, 3.5]),
        SimpleNamespace(id=3, name="Cata", career="Sistemas", grades=[4.8, 4.9]),
    ]

def test_filter_above_4():
    res = filter_by_average(s(), min_avg=4.0)
    assert all(r.average >= 4.0 for r in res)

def test_group_ranges():
    bins = [(0, 3.0), (3.0, 4.0), (4.0, 5.0)]
    g = group_by_ranges(s(), bins)
    assert "4.0-5.0" in g
    assert any(r.name == "Cata" for r in g["4.0-5.0"])
def test_filter_by_average_with_upper_limit():
    data = s()
    res = filter_by_average(data, max_avg=3.5)
    assert all(r.average <= 3.5 for r in res)

def test_group_by_ranges_edge_cases():
    data = s()
    bins = [(0, 3.0), (3.0, 4.0), (4.0, 5.0)]
    grouped = group_by_ranges(data, bins)
    # Todos los bins deben existir
    assert all(isinstance(v, list) for v in grouped.values())
    total_students = sum(len(v) for v in grouped.values())
    # No deben perderse estudiantes
    assert total_students == len(data)
