from student_manager.ranking import rank_students_global
from typing import Iterable, List, Dict, Tuple

def filter_by_average(students: Iterable, min_avg=None, max_avg=None):
    ranks = rank_students_global(students)
    result = []
    for r in ranks:
        if (min_avg is None or r.average >= min_avg) and (max_avg is None or r.average <= max_avg):
            result.append(r)
    return result

def group_by_ranges(students: Iterable, ranges: List[Tuple[float, float]]):
    groups: Dict[str, List] = {}
    ranks = rank_students_global(students)
    for low, high in ranges:
        label = f"{low:.1f}-{high:.1f}"
        groups[label] = [r for r in ranks if low <= r.average < high]
    return groups
