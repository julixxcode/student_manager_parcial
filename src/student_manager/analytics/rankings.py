from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class RankedStudent:
    name: str
    career: str
    average: float


def compute_averages_by_career(students: List[Any]) -> Dict[str, float]:
    """
    Calcula el promedio general por carrera.
    """
    data: Dict[str, List[float]] = {}

    for s in students:
        # Soporta tanto objetos como diccionarios
        career = getattr(s, "career", None) or s.get("career") or "Sin carrera"
        scores = getattr(s, "scores", None) or s.get("scores", [])
        if scores:
            data.setdefault(career, []).extend(scores)

    # Evita división por cero
    return {c: (sum(vals) / len(vals)) if vals else 0.0 for c, vals in data.items()}


def compute_rankings(
    students: List[Any],
    career: Optional[str] = None,
    top_n: int = 5
) -> List[RankedStudent]:
    """
    Genera un ranking de estudiantes ordenado por promedio.
    """
    results: List[RankedStudent] = []

    for s in students:
        # Admite tanto dict como objeto
        name = getattr(s, "name", None) or s.get("name")
        student_career = getattr(s, "career", None) or s.get("career")
        scores = getattr(s, "scores", None) or s.get("scores", [])

        # Ignorar sin notas o sin nombre
        if not name or not scores:
            continue

        # Filtro por carrera (insensible a mayúsculas)
        if career and student_career and student_career.lower() != career.lower():
            continue

        avg = sum(scores) / len(scores)
        results.append(RankedStudent(name, student_career, avg))

    # Orden descendente por promedio
    return sorted(results, key=lambda r: r.average, reverse=True)[:top_n]
