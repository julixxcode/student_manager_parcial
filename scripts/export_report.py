"""
Script para exportar un resumen del registro de estudiantes a formato de texto.
Ideal para generar reportes de avance o pruebas manuales.
"""

from student_manager.services import student_service
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

def export_students_report():
    students = student_service.list_students()
    if not students:
        print("⚠️ No hay datos para exportar.")
        return

    report_path = REPORTS_DIR / f"students_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        for s in students:
            file.write(f"{s['name']} ({s['career']}) - Promedio: {s['average']} - Estado: {s['status']}\n")

    print(f"✅ Reporte exportado con éxito en: {report_path}")

if __name__ == "__main__":
    export_students_report()
