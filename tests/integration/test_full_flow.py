from types import SimpleNamespace
from student_manager.ranking import rank_students_global
from student_manager.filters import filter_by_average
from student_manager.exporter import export_to_json
from student_manager.history import history_summary
import json

def test_full_flow(tmp_path):
    # Datos base
    students = [
        SimpleNamespace(id=1, name="Ana", career="Sistemas", grades=[4.5, 4.7, 4.8]),
        SimpleNamespace(id=2, name="Bruno", career="Civil", grades=[3.0, 3.2, 3.1]),
    ]

    # Ranking global
    ranks = rank_students_global(students)
    assert ranks[0].name == "Ana"

    # Filtro por promedio alto
    best = filter_by_average(students, min_avg=4.0)
    assert len(best) == 1 and best[0].name == "Ana"

    # Exportar a JSON
    out = tmp_path / "ranking.json"
    export_to_json(students, out)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert any("Ana" in d["name"] for d in data)

    # Historial individual
    summary = history_summary(students[0])
    assert summary["average"] > 4.0
