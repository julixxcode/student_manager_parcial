from statistics import mean
from dataclasses import dataclass
from typing import List, Iterable, Dict, Optional

@dataclass
class StudentRank:
    id: str
    name: str
    career: str
    average: float
    courses: int

def _get_grades(student) -> List[float]:
    grades = getattr(student, "grades", []) or []
    return [float(g) for g in grades if isinstance(g, (int, float))]

def rank_students_global(students: Iterable, min_courses: int = 1, top: Optional[int] = None) -> List[StudentRank]:
    ranks = []
    for s in students:
        grades = _get_grades(s)
        if len(grades) >= min_courses:
            ranks.append(StudentRank(
                id=str(getattr(s, "id", "")),
                name=str(getattr(s, "name", "")),
                career=str(getattr(s, "career", "")),
                average=round(mean(grades), 2),
                courses=len(grades)
            ))
    ranks.sort(key=lambda r: (-r.average, r.name))
    return ranks[:top] if top else ranks

def rank_students_by_career(students: Iterable) -> Dict[str, List[StudentRank]]:
    result = {}
    for r in rank_students_global(students):
        result.setdefault(r.career, []).append(r)
    return result
