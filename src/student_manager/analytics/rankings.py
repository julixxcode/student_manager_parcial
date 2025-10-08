from dataclasses import dataclass
from typing import Iterable, List, Dict, Optional, Any
from collections import defaultdict
from ..utils.students import get_student_average, get_student_career, get_student_name

@dataclass(frozen=True)
class RankedStudent:
    student: Any
    name: str
    career: str
    average: float

def compute_averages_by_career(students: Iterable[Any]) -> Dict[str, float]:
    sums, counts = defaultdict(float), defaultdict(int)
    for s in students:
        career = get_student_career(s) or "Sin carrera"
        avg = get_student_average(s)
        sums[career] += avg
        counts[career] += 1
    return {c: (sums[c] / counts[c]) if counts[c] else 0.0 for c in sums}

def compute_rankings(students: Iterable[Any], *, career: Optional[str] = None, top_n: int = 5) -> List[RankedStudent]:
    rows: List[RankedStudent] = []
    for s in students:
        c = get_student_career(s) or "Sin carrera"
        if career and c != career:
            continue
        avg = get_student_average(s)
        rows.append(RankedStudent(s, get_student_name(s), c, avg))
    rows.sort(key=lambda r: (-r.average, r.name.lower()))
    return rows[: max(1, int(top_n))]
