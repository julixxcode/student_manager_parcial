"""
Script auxiliar para reiniciar el archivo de datos de estudiantes.
Útil para pruebas o restaurar el estado inicial del sistema.
"""

import json
from student_manager.config import settings

def reset_data():
    with open(settings.STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4, ensure_ascii=False)
    print("✅ Archivo students.json reiniciado correctamente.")

if __name__ == "__main__":
    reset_data()
