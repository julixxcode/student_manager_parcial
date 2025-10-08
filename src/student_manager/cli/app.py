"""
CLI del sistema Student Manager.
Permite gestionar estudiantes desde la terminal con Typer y Rich.
Incluye operaciones CRUD, filtrado y estadísticas globales.
"""

import typer
from rich.console import Console
from rich.table import Table
from student_manager.services import student_service

app = typer.Typer(help="📘 Sistema de Gestión de Estudiantes")
console = Console()

# ============================================================
# 🔹 CREAR ESTUDIANTE
# ============================================================
@app.command()
def add():
    """Agrega un nuevo estudiante al sistema."""
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

# ============================================================
# 🔹 LISTAR ESTUDIANTES
# ============================================================
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
    table.add_column("Creado", justify="center")
    table.add_column("Actualizado", justify="center")

    for s in students:
        table.add_row(
            s["id"], s["name"], str(s["age"]),
            s["career"], str(s["average"]), s["status"],
            s.get("created_at", "-"), s.get("updated_at", "-")
        )

    console.print(table)

# ============================================================
# 🔹 FILTRAR ESTUDIANTES
# ============================================================
@app.command()
def filter(career: str = typer.Option(None, help="Filtrar por carrera"),
           status: str = typer.Option(None, help="Filtrar por estado: Aprobado o Reprobado")):
    """Filtra estudiantes por carrera o estado académico."""
    results = student_service.filter_students(career, status)

    if not results:
        console.print("[yellow]⚠️ No se encontraron estudiantes con esos criterios.[/yellow]")
        return

    table = Table(title="🎯 Estudiantes Filtrados")
    table.add_column("ID", style="cyan")
    table.add_column("Nombre")
    table.add_column("Carrera")
    table.add_column("Promedio")
    table.add_column("Estado")

    for s in results:
        table.add_row(s["id"], s["name"], s["career"], str(s["average"]), s["status"])

    console.print(table)

# ============================================================
# 🔹 BUSCAR ESTUDIANTE POR ID
# ============================================================
@app.command()
def get(student_id: str):
    """Busca un estudiante por su ID."""
    s = student_service.find_student(student_id)
    if not s:
        console.print(f"[red]❌ No se encontró estudiante con ID {student_id}[/red]")
    else:
        console.print(f"[bold green]Estudiante encontrado:[/bold green]")
        console.print(s)

# ============================================================
# 🔹 ACTUALIZAR ESTUDIANTE
# ============================================================
@app.command()
def update(student_id: str):
    """Actualiza los datos básicos del estudiante."""
    name = typer.prompt("Nuevo nombre (Enter para omitir)", default=None)
    age = typer.prompt("Nueva edad (Enter para omitir)", default=None)
    career = typer.prompt("Nueva carrera (Enter para omitir)", default=None)
    ok = student_service.modify_student(student_id, name=name, age=age, career=career)
    console.print("✅ Estudiante actualizado" if ok else "⚠️ No se encontró el ID especificado.")

# ============================================================
# 🔹 ELIMINAR ESTUDIANTE
# ============================================================
@app.command()
def delete(student_id: str):
    """Elimina un estudiante por su ID."""
    ok = student_service.remove_student(student_id)
    console.print("🗑️ Estudiante eliminado" if ok else "⚠️ No se encontró ningún estudiante con ese ID.")

# ============================================================
# 🔹 ESTADÍSTICAS GLOBALES
# ============================================================
@app.command()
def stats():
    """Muestra estadísticas generales del sistema."""
    stats = student_service.get_statistics()
    console.print("\n📊 [bold underline]Estadísticas Generales[/bold underline]\n")
    console.print(f"👥 Total de estudiantes: [cyan]{stats['total']}[/cyan]")
    console.print(f"📈 Promedio general: [green]{stats['average']}[/green]")
    console.print(f"✅ Aprobados: [bold green]{stats['approved']}[/bold green]")
    console.print(f"❌ Reprobados: [bold red]{stats['reproved']}[/bold red]")

# ============================================================
# 🔹 PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    app()
