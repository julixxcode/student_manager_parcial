"""
CLI del sistema Student Manager.
Permite gestionar estudiantes desde la terminal con Typer y Rich.
"""

import typer
from rich.console import Console
from rich.table import Table
from student_manager.services import student_service

app = typer.Typer(help="📘 Sistema de Gestión de Estudiantes")
console = Console()

@app.command()
def add():
    """Agrega un nuevo estudiante."""
    try:
        name = typer.prompt("Nombre del estudiante")
        age = typer.prompt("Edad", type=int)
        career = typer.prompt("Carrera")
        grades = typer.prompt("Notas separadas por coma (ej: 4.0,3.5,5.0)")
        grades_list = [float(g.strip()) for g in grades.split(",")]

        student = student_service.create_student(name, age, career, grades_list)
        console.print(f"✅ Estudiante [bold]{student['name']}[/bold] creado con éxito. ID: {student['id']}")
    except Exception as e:
        console.print(f"[red]{e}[/red]")

@app.command()
def list():
    """Muestra todos los estudiantes registrados."""
    students = student_service.list_students()
    if not students:
        console.print("[yellow]⚠️ No hay estudiantes registrados aún.[/yellow]")
        return

    table = Table(title="📋 Lista de Estudiantes Registrados")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Nombre", style="bold")
    table.add_column("Edad", justify="center")
    table.add_column("Carrera")
    table.add_column("Promedio", justify="center")
    table.add_column("Estado", justify="center")

    for s in students:
        table.add_row(
            s["id"], s["name"], str(s["age"]),
            s["career"], str(s["average"]), s["status"]
        )

    console.print(table)

@app.command()
def get(student_id: str):
    """Busca un estudiante por su ID."""
    s = student_service.find_student(student_id)
    if not s:
        console.print(f"[red]❌ No se encontró estudiante con ID {student_id}[/red]")
    else:
        console.print(f"[bold green]Estudiante encontrado:[/bold green]\n{s}")

@app.command()
def update(student_id: str):
    """Actualiza los datos básicos del estudiante."""
    name = typer.prompt("Nuevo nombre (Enter para omitir)", default=None)
    age = typer.prompt("Nueva edad (Enter para omitir)", default=None)
    career = typer.prompt("Nueva carrera (Enter para omitir)", default=None)
    ok = student_service.modify_student(student_id, name=name, age=age, career=career)
    console.print("✅ Estudiante actualizado" if ok else "⚠️ No se encontró el ID especificado.")

@app.command()
def delete(student_id: str):
    """Elimina un estudiante por su ID."""
    ok = student_service.remove_student(student_id)
    console.print("🗑️ Estudiante eliminado" if ok else "⚠️ No se encontró ningún estudiante con ese ID.")

if __name__ == "__main__":
    app()
