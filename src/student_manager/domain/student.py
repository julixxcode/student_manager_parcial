"""
Define la entidad Student con atributos, validaciones
y métodos de negocio (promedio y estado académico).
"""

import uuid
from statistics import mean
from student_manager.utils import validators

class Student:
    """Clase que representa un estudiante dentro del sistema."""

    def __init__(self, name: str, age: int, career: str, grades: list[float]):
        # Validaciones robustas de entrada
        if not validators.validate_name(name):
            raise ValueError("❌ Nombre inválido. Debe tener al menos 2 caracteres.")
        if not validators.validate_age(age):
            raise ValueError("❌ Edad fuera de rango (debe estar entre 10 y 100).")
        if not validators.validate_grades(grades):
            raise ValueError("❌ Notas inválidas o fuera del rango permitido (0 a 5).")

        # Asignación de atributos
        self.id = str(uuid.uuid4())[:8]
        self.name = name.strip().title()
        self.age = age
        self.career = career.strip().title()
        self.grades = grades

    def average(self) -> float:
        """Calcula el promedio redondeado a dos decimales."""
        return round(mean(self.grades), 2)

    def status(self) -> str:
        """Devuelve el estado del estudiante (Aprobado/Reprobado)."""
        return "Aprobado" if self.average() >= 3.0 else "Reprobado"

    def to_dict(self) -> dict:
        """Convierte el objeto a un diccionario serializable (para JSON)."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "career": self.career,
            "grades": self.grades,
            "average": self.average(),
            "status": self.status(),
        }

    def __str__(self):
        """Representación legible del estudiante."""
        return f"{self.name} ({self.career}) - Promedio: {self.average()} ({self.status()})"
