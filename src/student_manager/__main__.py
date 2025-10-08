"""
Punto de entrada principal del sistema Student Manager.
Permite ejecutar la aplicación directamente con:
    python -m student_manager
"""

from student_manager.cli.app import app

if __name__ == "__main__":
    app()
