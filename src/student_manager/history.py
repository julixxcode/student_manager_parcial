from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class HistoryEntry:
    term: str
    course: str
    grade: float

def get_history(student) -> List[HistoryEntry]:
    history = []
    if hasattr(student, "history") and student.history:
        for record in student.history:
            history.append(HistoryEntry(
                term=str(record.get("term", "")),
                course=str(record.get("course", "")),
                grade=float(record.get("grade", 0))
            ))
    else:
        for i, g in enumerate(getattr(student, "grades", []), start=1):
            history.append(HistoryEntry(term=f"T{i}", course=f"Curso {i}", grade=float(g)))
    return history

def history_summary(student) -> Dict[str, Any]:
    h = get_history(student)
    if not h:
        return {"count": 0, "average": 0, "best": None, "worst": None}
    grades = [e.grade for e in h]
    return {
        "count": len(h),
        "average": round(sum(grades) / len(grades), 2),
        "best": max(grades),
        "worst": min(grades),
    }
