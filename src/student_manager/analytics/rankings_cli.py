import argparse, json, sys
from typing import List, Any, Optional

from .rankings import compute_averages_by_career, compute_rankings, RankedStudent

# ---------------------------------------------------------------------------
# 🔹 Función para cargar estudiantes (desde CSV o datos de demo)
# ---------------------------------------------------------------------------
def _load_students(csv_path: Optional[str] = None) -> List[Any]:
    if csv_path:
        try:
            from ..repositories.import_csv import import_from_csv
            return list(import_from_csv(csv_path))
        except Exception as e:
            print(f"[WARN] No se pudo leer CSV '{csv_path}': {e}. Se usarán datos de demo.", file=sys.stderr)

    # Datos de demostración (por si no hay CSV)
    class Demo:
        def __init__(self, name, career, scores):
            self.name = name
            self.career = career
            self.scores = scores

    return [
        Demo("Ana", "Sistemas", [4.5, 4.2, 4.8]),
        Demo("Luis", "Sistemas", [3.9, 4.0, 4.1]),
        Demo("María", "Industrial", [4.7, 4.6, 4.8]),
        Demo("Carlos", "Industrial", [3.5, 3.6, 3.7]),
        Demo("Sofi", "Diseño", [4.9, 4.8]),
    ]


# ---------------------------------------------------------------------------
# 🔹 Impresiones con Rich (si está disponible)
# ---------------------------------------------------------------------------
def _print_averages(averages: dict):
    try:
        from rich.console import Console
        from rich.table import Table

        table = Table(title="Promedio por carrera")
        table.add_column("Carrera", style="bold")
        table.add_column("Promedio", justify="right")

        for c, avg in sorted(averages.items()):
            table.add_row(c, f"{avg:.2f}")

        Console().print(table)
    except Exception:
        print("== Promedios por carrera ==")
        for c, avg in sorted(averages.items()):
            print(f"- {c}: {avg:.2f}")


def _print_top(rows: List[RankedStudent], title: str):
    try:
        from rich.console import Console
        from rich.table import Table

        table = Table(title=title)
        table.add_column("#", justify="right")
        table.add_column("Nombre", style="bold")
        table.add_column("Carrera")
        table.add_column("Promedio", justify="right")

        for i, r in enumerate(rows, start=1):
            table.add_row(str(i), r.name, r.career, f"{r.average:.2f}")

        Console().print(table)
    except Exception:
        print(title)
        for i, r in enumerate(rows, start=1):
            print(f"{i}. {r.name} | {r.career} | {r.average:.2f}")


# ---------------------------------------------------------------------------
# 🔹 CLI principal con argparse
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Analytics CLI (promedios y rankings).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # -------------------
    # Comando: by-career
    # -------------------
    p1 = sub.add_parser("by-career", help="Promedio de cada carrera")
    p1.add_argument("--csv", type=str, default=None, help="Ruta a CSV para cargar estudiantes")
    p1.add_argument("--export-csv", type=str, default=None, help="Guardar promedios en CSV")
    p1.add_argument("--export-json", type=str, default=None, help="Guardar promedios en JSON")

    # -------------------
    # Comando: top
    # -------------------
    p2 = sub.add_parser("top", help="Top N estudiantes")
    p2.add_argument("--csv", type=str, default=None, help="Ruta a CSV para cargar estudiantes")
    p2.add_argument("-n", "--top", type=int, default=5, help="Cantidad de estudiantes a mostrar")
    p2.add_argument("-c", "--career", type=str, default=None, help="Filtrar por carrera")
    p2.add_argument("--export-csv", type=str, default=None, help="Guardar ranking en CSV")
    p2.add_argument("--export-json", type=str, default=None, help="Guardar ranking en JSON")

    # -------------------
    # Comando: report
    # -------------------
    p3 = sub.add_parser("report", help="Generar reporte HTML con gráficas")
    p3.add_argument("--csv", type=str, default=None, help="Ruta a CSV para cargar estudiantes")
    p3.add_argument("-n", "--top", type=int, default=10, help="Cantidad de estudiantes en el top")
    p3.add_argument("-c", "--career", type=str, default=None, help="Filtrar por carrera")
    p3.add_argument("-o", "--output", type=str, default="out/reporte_analytics.html", help="Ruta del HTML a generar")

    args = parser.parse_args(argv)

    # ---------------------------------------------------------------
    # Lógica de ejecución según el subcomando
    # ---------------------------------------------------------------
    students = _load_students(args.csv)

    if args.cmd == "by-career":
        averages = compute_averages_by_career(students)
        _print_averages(averages)

        # Exportar si se solicita
        if args.export_csv or args.export_json:
            from ..reports.exporters import export_averages_csv, export_averages_json
            if args.export_csv:
                p = export_averages_csv(averages, args.export_csv)
                print(f"[OK] CSV generado en: {p}")
            if args.export_json:
                p = export_averages_json(averages, args.export_json)
                print(f"[OK] JSON generado en: {p}")
        return 0

    if args.cmd == "top":
        rows = compute_rankings(students, career=args.career, top_n=args.top)
        title = f"Top {args.top} estudiantes" + (f" de {args.career}" if args.career else "")
        _print_top(rows, title)

        # Exportar si se solicita
        if args.export_csv or args.export_json:
            from ..reports.exporters import export_rankings_csv, export_rankings_json
            if args.export_csv:
                p = export_rankings_csv(rows, args.export_csv)
                print(f"[OK] CSV generado en: {p}")
            if args.export_json:
                p = export_rankings_json(rows, args.export_json)
                print(f"[OK] JSON generado en: {p}")
        return 0

    if args.cmd == "report":
        from ..reports.html_report import generate_rankings_report
        out = generate_rankings_report(
            students,
            output_html=args.output,
            top_n=args.top,
            career=args.career,
        )
        print(f"[OK] Reporte generado en: {out}")
        return 0

    return 1


# ---------------------------------------------------------------------------
# 🔹 Punto de entrada
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    raise SystemExit(main())
