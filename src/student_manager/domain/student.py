from dataclasses import dataclass, field
from typing import List
import uuid

@dataclass
class Student:
    """Representa a un estudiante con sus datos básicos y notas."""

    name: str
    age: int
    career: str
    grades: List[float] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])

    def average(self) -> float:
        """Calcula el promedio de las notas del estudiante."""
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)

    def status(self) -> str:
        """Devuelve el estado del estudiante (Aprobado o Reprobado)."""
        return "Aprobado" if self.average() >= 3.0 else "Reprobado"

    def to_dict(self) -> dict:
        """Convierte el objeto Student a un diccionario listo para guardar."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "career": self.career,
            "grades": self.grades,
            "average": self.average(),
            "status": self.status(),
        }
