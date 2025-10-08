from __future__ import annotations
from pathlib import Path
from typing import Any, Optional, List, Dict
from datetime import datetime

import matplotlib.pyplot as plt

from ..analytics.rankings import compute_averages_by_career, compute_rankings

def _ensure_out_file(path: str | Path) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def _plot_bar_from_mapping(mapping: Dict[str, float], out_png: Path) -> Path:
    # Grafica 1: promedio por carrera
    fig = plt.figure()
    careers = list(mapping.keys())
    values = [mapping[c] for c in careers]
    plt.bar(careers, values)
    plt.xticks(rotation=45, ha="right")
    plt.title("Promedio por carrera")
    plt.ylabel("Promedio")
    fig.tight_layout()
    fig.savefig(out_png, dpi=120)
    plt.close(fig)
    return out_png

def _plot_barh_top(rows: List[Any], out_png: Path) -> Path:
    # Grafica 2: top N (horizontal)
    names = [getattr(r, "name", None) or r.get("name") for r in rows]
    values = [float(getattr(r, "average", None) or r.get("average", 0.0)) for r in rows]
    fig = plt.figure()
    plt.barh(names, values)
    plt.gca().invert_yaxis()
    plt.xlabel("Promedio")
    plt.title("Top estudiantes")
    fig.tight_layout()
    fig.savefig(out_png, dpi=120)
    plt.close(fig)
    return out_png

def generate_rankings_report(
    students: List[Any],
    *,
    output_html: str | Path = "out/reporte_analytics.html",
    top_n: int = 10,
    career: Optional[str] = None,
    title: str = "Reporte Académico"
) -> Path:
    out_html = _ensure_out_file(output_html)
    out_dir = out_html.parent

    # Datos
    averages = compute_averages_by_career(students)
    top_rows = compute_rankings(students, career=career, top_n=top_n)

    # Gráficos
    avg_png = _plot_bar_from_mapping(averages, out_dir / "avg_by_career.png")
    top_png = _plot_barh_top(top_rows, out_dir / "top_students.png")

    # HTML simple
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    rows_html = "\n".join(
        f"<tr><td>{i}</td><td>{getattr(r, 'name', None)}</td><td>{getattr(r, 'career', None)}</td><td>{getattr(r,'average',0):.2f}</td></tr>"
        for i, r in enumerate(top_rows, start=1)
    )
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
 body {{ font-family: Arial, sans-serif; margin: 20px; }}
 h1, h2 {{ margin: 0.4rem 0; }}
 .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
 table {{ border-collapse: collapse; width: 100%; }}
 th, td {{ border: 1px solid #ccc; padding: 6px 8px; text-align: left; }}
 th {{ background: #f6f6f6; }}
 small {{ color: #666; }}
 img {{ max-width: 100%; height: auto; border: 1px solid #eee; }}
</style>
</head>
<body>
  <h1>{title}</h1>
  <small>Generado: {now}</small>

  <h2>Promedio por carrera</h2>
  <img src="{avg_png.name}" alt="Promedio por carrera">

  <h2>Top {top_n} estudiantes {('de ' + career) if career else ''}</h2>
  <div class="grid">
    <div>
      <img src="{top_png.name}" alt="Top estudiantes">
    </div>
    <div>
      <table>
        <thead><tr><th>#</th><th>Nombre</th><th>Carrera</th><th>Promedio</th></tr></thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>
    </div>
  </div>
</body>
</html>"""
    out_html.write_text(html, encoding="utf-8")
    return out_html
