import csv, json
from student_manager.ranking import rank_students_global

def export_to_csv(students, filename):
    ranks = rank_students_global(students)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "career", "average", "courses"])
        writer.writeheader()
        for r in ranks:
            writer.writerow(r.__dict__)
    return filename

def export_to_json(students, filename):
    ranks = [r.__dict__ for r in rank_students_global(students)]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(ranks, f, ensure_ascii=False, indent=2)
    return filename
