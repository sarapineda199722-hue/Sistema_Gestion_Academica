class EstudianteYaMatriculadoError(Exception):
    """El estudiante ya está matriculado en el grupo."""
    pass


class GrupoLlenoError(Exception):
    """El grupo alcanzó su capacidad máxima."""
    pass


class EstudianteNoMatriculadoError(Exception):
    """El estudiante que se desea retirar no está matriculado."""
    pass


class AsignaturaNoEncontradaError(Exception):
    """La asignatura buscada no existe."""
    pass


class ProgramaNoEncontradoError(Exception):
    """El programa académico buscado no existe."""
    pass
