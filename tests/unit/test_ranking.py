from types import SimpleNamespace
from student_manager.ranking import rank_students_global, rank_students_by_career
import pytest
from student_manager.ranking import StudentRank

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
def test_studentrank_dataclass_equality():
    a = StudentRank(id="1", name="Ana", career="Sistemas", average=4.5, courses=3)
    b = StudentRank(id="1", name="Ana", career="Sistemas", average=4.5, courses=3)
    assert a == b  # dataclasses son comparables por valor

def test_rank_students_with_non_numeric_grades():
    data = [
        SimpleNamespace(id=1, name="Ana", career="Sistemas", grades=["A", None, 4.0]),
    ]
    result = rank_students_global(data)
    assert len(result) == 1
    assert result[0].average == 4.0  # ignora valores no numéricos

def test_rank_students_global_tie_break_by_name():
    data = [
        SimpleNamespace(id=1, name="Zoe", career="Civil", grades=[4.0, 4.0]),
        SimpleNamespace(id=2, name="Ana", career="Civil", grades=[4.0, 4.0]),
    ]
    ranks = rank_students_global(data)
    assert ranks[0].name == "Ana"  # en empate gana por nombre alfabéticamente