from types import SimpleNamespace
from student_manager.ranking import rank_students_global, rank_students_by_career

def sample_students():
    return [
        SimpleNamespace(id=1, name="Ana", career="Sistemas", grades=[4.5, 4.7, 4.3]),
        SimpleNamespace(id=2, name="Bruno", career="Civil", grades=[3.5, 3.0]),
        SimpleNamespace(id=3, name="Cata", career="Sistemas", grades=[4.9, 4.8]),
    ]

def test_rank_global_top_order():
    ranks = rank_students_global(sample_students())
    assert ranks[0].name == "Cata"
    assert ranks[1].name == "Ana"

def test_rank_by_career_groups():
    ranks = rank_students_by_career(sample_students())
    assert "Sistemas" in ranks
    assert "Civil" in ranks
    assert ranks["Sistemas"][0].name == "Cata"
