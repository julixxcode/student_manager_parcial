from typing import Any, Iterable, Optional

def _safe_mean(nums: Iterable[float]) -> float:
    nums = [x for x in nums if x is not None]
    return sum(nums) / len(nums) if nums else 0.0

def get_student_average(student: Any) -> float:
    """Obtiene el promedio de un estudiante, tolerando distintos modelos."""
    if hasattr(student, "average"):
        avg = getattr(student, "average")
        return avg() if callable(avg) else float(avg)
    if hasattr(student, "get_average") and callable(student.get_average):
        return float(student.get_average())
    for attr in ("scores", "grades", "notas"):
        if hasattr(student, attr):
            vals = getattr(student, attr)
            try:
                return _safe_mean(float(v) for v in vals)
            except Exception:
                pass
    keys = [k for k in dir(student) if k.lower().startswith("score")]
    if keys:
        vals = []
        for k in keys:
            try:
                vals.append(float(getattr(student, k)))
            except Exception:
                pass
        if vals:
            return _safe_mean(vals)
    return 0.0

def get_student_career(student: Any) -> Optional[str]:
    for attr in ("career", "carrera", "major", "program"):
        if hasattr(student, attr):
            val = getattr(student, attr)
            if val:
                return str(val)
    return None

def get_student_name(student: Any) -> str:
    for attr in ("name", "nombre", "full_name"):
        if hasattr(student, attr):
            val = getattr(student, attr)
            if val:
                return str(val)
    return getattr(student, "id", None) and f"ID {getattr(student,'id')}" or repr(student)
