import pytest
from src.student_manager.analytics.rankings import compute_averages_by_career, compute_rankings, RankedStudent

# ------------------------------------------------------------
# 🔹 Casos de prueba adicionales para analytics/rankings.py
# ------------------------------------------------------------

def test_compute_averages_by_career_multiple_students():
    students = [
        {"name": "Ana", "career": "Sistemas", "scores": [4.0, 4.2]},
        {"name": "Luis", "career": "Sistemas", "scores": [3.8, 4.0]},
        {"name": "Carlos", "career": "Industrial", "scores": [4.5, 4.7]},
    ]
    result = compute_averages_by_career(students)
    assert "Sistemas" in result
    assert "Industrial" in result
    assert round(result["Sistemas"], 2) == 4.0
    assert round(result["Industrial"], 2) == 4.6


def test_compute_rankings_top3_sorted_correctly():
    students = [
        {"name": "Ana", "career": "Sistemas", "scores": [4.5, 4.0]},
        {"name": "Luis", "career": "Sistemas", "scores": [3.9, 4.1]},
        {"name": "Sofi", "career": "Diseño", "scores": [4.9, 4.8]},
    ]
    result = compute_rankings(students, top_n=3)
    assert len(result) == 3
    assert isinstance(result[0], RankedStudent)
    assert result[0].name == "Sofi"
    assert result[1].average >= result[2].average


def test_compute_rankings_filter_by_career_case_insensitive():
    students = [
        {"name": "Ana", "career": "Sistemas", "scores": [4.5, 4.0]},
        {"name": "Luis", "career": "Industrial", "scores": [3.9, 4.1]},
        {"name": "Sofi", "career": "Diseño", "scores": [4.9, 4.8]},
    ]
    result = compute_rankings(students, career="sistemas", top_n=5)
    assert len(result) == 1
    assert result[0].career.lower() == "sistemas"


def test_compute_rankings_ignore_students_without_scores():
    students = [
        {"name": "Ana", "career": "Sistemas", "scores": []},
        {"name": "Luis", "career": "Industrial", "scores": [3.9, 4.1]},
        {"name": "Sofi", "career": "Diseño", "scores": [4.9, 4.8]},
    ]
    result = compute_rankings(students)
    assert all(r.average > 0 for r in result)
    names = [r.name for r in result]
    assert "Ana" not in names


def test_compute_rankings_empty_list_returns_empty():
    result = compute_rankings([])
    assert result == []
