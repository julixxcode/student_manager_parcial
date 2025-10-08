from typer.testing import CliRunner
from student_manager.cli.app import app
from student_manager.services import student_service
import pytest

runner = CliRunner()

@pytest.fixture(autouse=True)
def setup(monkeypatch, tmp_path):
    fake_file = tmp_path / "students.json"
    monkeypatch.setattr(student_service.settings, "STUDENTS_FILE", fake_file)
    student_service.create_student("Julian", 22, "Software", [4, 5, 4])
    yield

def test_cli_list_command():
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "Julian" in result.stdout

def test_cli_stats_command():
    result = runner.invoke(app, ["stats"])
    assert result.exit_code == 0
    assert "Estadísticas" in result.stdout
