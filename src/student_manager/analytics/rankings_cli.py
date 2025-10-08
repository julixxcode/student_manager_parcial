import argparse, json
from typing import List, Any, Optional
from .rankings import compute_averages_by_career, compute_rankings

def _load_demo_students() -> List[Any]:
    class Demo:
        def __init__(self, name, career, scores):
            self.name = name; self.career = career; self.scores = scores
    return [
        Demo("Ana", "Sistemas", [4.5, 4.2, 4.8]),
        Demo("Luis", "Sistemas", [3.9, 4.0, 4.1]),
        Demo("María", "Industrial", [4.7, 4.6, 4.8]),
        Demo("Carlos", "Industrial", [3.5, 3.6, 3.7]),
        Demo("Sofi", "Diseño", [4.9, 4.8]),
    ]

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="CLI para rankings de estudiantes.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("by-career", help="Promedio de cada carrera")
    p2 = sub.add_parser("top", help="Top N estudiantes")
    p2.add_argument("-n", "--top", type=int, default=5)
    p2.add_argument("-c", "--career", type=str, default=None)
    args = parser.parse_args(argv)

    students = _load_demo_students()

    if args.cmd == "by-career":
        data = compute_averages_by_career(students)
        print("== Promedios por carrera ==")
        for c, avg in data.items():
            print(f"- {c}: {avg:.2f}")
        return 0

    if args.cmd == "top":
        rows = compute_rankings(students, career=args.career, top_n=args.top)
        print(f"== Top {args.top} estudiantes ==")
        for i, r in enumerate(rows, start=1):
            print(f"{i}. {r.name} | {r.career} | {r.average:.2f}")
        return 0

    return 1

if __name__ == "__main__":
    raise SystemExit(main())
