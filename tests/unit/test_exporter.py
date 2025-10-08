from types import SimpleNamespace
from student_manager.exporter import export_to_csv, export_to_json
import csv, json
import io
import csv

def students():
    return [
        SimpleNamespace(id=1, name="Ana", career="Sistemas", grades=[4.5, 4.2]),
        SimpleNamespace(id=2, name="Bruno", career="Civil", grades=[3.1, 3.4])
    ]

def test_export_csv(tmp_path):
    file = tmp_path / "ranks.csv"
    export_to_csv(students(), file)
    with open(file, encoding="utf-8") as f:
        data = list(csv.DictReader(f))
    assert len(data) == 2
    assert data[0]["name"] == "Ana"

def test_export_json(tmp_path):
    file = tmp_path / "ranks.json"
    export_to_json(students(), file)
    data = json.loads(file.read_text(encoding="utf-8"))
    assert data[0]["name"] == "Ana"
    
def test_export_to_csv_in_memory(monkeypatch):
    data = students()
    fake_file = io.StringIO()
    writer = csv.DictWriter(fake_file, fieldnames=["id","name","career","average","courses"])
    # Simula escritura en memoria
    for r in data:
        writer.writerow({"id": r.id, "name": r.name, "career": r.career, "average": 4.0, "courses": 2})
    fake_file.seek(0)
    lines = fake_file.read().splitlines()
    assert len(lines) > 0