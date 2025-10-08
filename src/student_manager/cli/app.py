import typer
from rich.console import Console
from rich.table import Table
from typing import Optional, List

from student_manager.services import student_service as svc

app = typer.Typer(help="Sistema de Gestión de Estudiantes")
console = Console()


def _parse_grades(grades: Optional[str]) -> List[float]:
    """Convierte una cadena como '4.0,3.5,5.0' en una lista [4.0, 3.5, 5.0]."""
    if not grades:
        return []
    try:
        return [float(x.strip()) for x in grades.split(",") if x.strip()]
    except ValueError:
        console.print("[red]❌ Error:[/red] Las notas deben ser números separados por comas.")
        raise typer.Exit()


@app.command("add")
def add_student(
    name: str = typer.Option(..., prompt=True, help="Nombre del estudiante"),
    age: int = typer.Option(..., prompt=True, help="Edad"),
    career: str = typer.Option(..., prompt=True, help="Carrera"),
    grades: str = typer.Option("", prompt="Notas (ej: 4.0,3.5,5.0)", help="Notas separadas por coma"),
):
    """Agrega un nuevo estudiante al sistema."""
    student = svc.create_student(name, age, career, _parse_grades(grades))
    console.print(f"[green]✅ Estudiante creado:[/green] {student['id']} ({student['name']})")


@app.command("list")
def list_students():
    """Muestra todos los estudiantes registrados."""
    data = svc.list_students()
    if not data:
        console.print("[yellow]⚠️ No hay estudiantes registrados aún.[/yellow]")
        return

    table = Table(title="Lista de Estudiantes")
    for col in ["ID", "Nombre", "Edad", "Carrera", "Promedio", "Estado"]:
        table.add_column(col, style="cyan")
    for s in data:
        table.add_row(
            s["id"],
            s["name"],
            str(s["age"]),
            s["career"],
            str(s["average"]),
            s["status"],
        )
    console.print(table)


@app.command("get")
def get_student(student_id: str):
    """Busca un estudiante por su ID."""
    student = svc.find_student(student_id)
    if not student:
        console.print("[red]❌ Estudiante no encontrado.[/red]")
        raise typer.Exit()

    console.print(student)


@app.command("update")
def update_student(
    student_id: str = typer.Argument(..., help="ID del estudiante a modificar"),
    name: Optional[str] = typer.Option(None, help="Nuevo nombre"),
    age: Optional[int] = typer.Option(None, help="Nueva edad"),
    career: Optional[str] = typer.Option(None, help="Nueva carrera"),
    grades: Optional[str] = typer.Option(None, help="Nuevas notas (ej: 3.5,4.0,4.5)"),
):
    """Actualiza los datos de un estudiante."""
    ok = svc.modify_student(
        student_id,
        name=name,
        age=age,
        career=career,
        grades=_parse_grades(grades) if grades else None,
    )
    console.print("[green]✅ Estudiante actualizado.[/green]" if ok else "[red]❌ No se encontró el estudiante.[/red]")


@app.command("delete")
def delete_student(student_id: str):
    """Elimina un estudiante del sistema."""
    ok = svc.remove_student(student_id)
    console.print("[green]🗑️ Estudiante eliminado.[/green]" if ok else "[red]❌ No se encontró el estudiante.[/red]")


if __name__ == "__main__":
    app()
