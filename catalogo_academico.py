from excepciones import (
    AsignaturaNoEncontradaError,
    ProgramaNoEncontradoError
)


class CatalogoAcademico:
    """Guarda programas y asignaturas y permite buscarlos por código."""

    def __init__(self):
        self.__programas = {}
        self.__asignaturas = {}

    def agregar_programa(self, programa):
        self.__programas[programa.get_codigo()] = programa

    def agregar_asignatura(self, asignatura):
        self.__asignaturas[asignatura.get_codigo()] = asignatura

    def buscar_programa(self, codigo):
        if codigo not in self.__programas:
            raise ProgramaNoEncontradoError(
                f"No existe un programa académico con el código {codigo}."
            )

        return self.__programas[codigo]

    def buscar_asignatura(self, codigo):
        if codigo not in self.__asignaturas:
            raise AsignaturaNoEncontradaError(
                f"No existe una asignatura con el código {codigo}."
            )

        return self.__asignaturas[codigo]
    