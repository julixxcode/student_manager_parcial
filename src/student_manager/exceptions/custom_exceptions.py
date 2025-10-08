"""
Definición de excepciones personalizadas para el sistema Student Manager.
Permiten manejar errores de validación y persistencia de forma controlada.
"""

class ValidationError(Exception):
    """Error lanzado al validar datos incorrectos."""
    def __init__(self, message: str):
        super().__init__(f"Error de validación: {message}")

class RepositoryError(Exception):
    """Error lanzado al acceder o modificar los datos persistidos."""
    def __init__(self, message: str):
        super().__init__(f"Error de repositorio: {message}")
