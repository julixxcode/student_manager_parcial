from __future__ import annotations
from pathlib import Path
from typing import Iterable, Any, Dict, List
import csv, json

def _ensure_out_path(out_path: Path | str) -> Path:
    p = Path(out_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def _row_to_dict(row: Any) -> Dict[str, Any]:
    """Acepta RankedStudent o dict con name/career/average."""
    if isinstance(row, dict):
        return {
            "name": row.get("name"),
            "career": row.get("career"),
            "average": float(row.get("average", 0.0)),
        }
    # objeto con atributos
    name = getattr(row, "name", None)
    career = getattr(row, "career", None)
    avg = getattr(row, "average", None)
    return {"name": name, "career": career, "average": float(avg or 0.0)}

# ---------- Averages ----------
def export_averages_csv(averages: Dict[str, float], out_path: str | Path) -> Path:
    p = _ensure_out_path(out_path)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["career", "average"])
        for career, avg in averages.items():
            w.writerow([career, f"{avg:.2f}"])
    return p

def export_averages_json(averages: Dict[str, float], out_path: str | Path) -> Path:
    p = _ensure_out_path(out_path)
    p.write_text(json.dumps(averages, ensure_ascii=False, indent=2), encoding="utf-8")
    return p

# ---------- Rankings ----------
def export_rankings_csv(rows: Iterable[Any], out_path: str | Path) -> Path:
    p = _ensure_out_path(out_path)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "name", "career", "average"])
        for i, r in enumerate(rows, start=1):
            d = _row_to_dict(r)
            w.writerow([i, d["name"], d["career"], f"{d['average']:.2f}"])
    return p

def export_rankings_json(rows: Iterable[Any], out_path: str | Path) -> Path:
    p = _ensure_out_path(out_path)
    payload: List[Dict[str, Any]] = []
    for i, r in enumerate(rows, start=1):
        d = _row_to_dict(r)
        payload.append({"rank": i, **d})
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return p
