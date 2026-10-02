from horario import Horario
from excepciones import (
    EstudianteYaMatriculadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError
)


class GrupoAcademico:
    """Organiza una asignatura, su docente, horario y estudiantes."""

    def __init__(
        self,
        codigo,
        asignatura,
        docente,
        capacidad_maxima,
        dia,
        hora_inicio,
        hora_finalizacion,
        salon
    ):
        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser mayor que cero.")

        self.__codigo = codigo
        self.__asignatura = asignatura
        self.__docente = docente
        self.__capacidad_maxima = capacidad_maxima
        self.__estudiantes = []

        # Composición: el grupo crea y contiene su propio horario.
        self.__horario = Horario(
            dia,
            hora_inicio,
            hora_finalizacion,
            salon
        )

    def mostrar_informacion_grupo(self):
        print(f"Código del grupo: {self.__codigo}")
        print(f"Asignatura: {self.__asignatura.get_nombre()}")
        print(f"Docente: {self.__docente.get_nombre()}")
        print(f"Capacidad máxima: {self.__capacidad_maxima}")
        print(f"Estudiantes matriculados: {len(self.__estudiantes)}")
        self.__horario.mostrar_informacion()

    def matricular_estudiante(self, estudiante):
        codigo = estudiante.get_codigo_estudiantil()

        for matriculado in self.__estudiantes:
            if matriculado.get_codigo_estudiantil() == codigo:
                raise EstudianteYaMatriculadoError(
                    f"El estudiante {codigo} ya está matriculado "
                    f"en el grupo {self.__codigo}."
                )

        if len(self.__estudiantes) >= self.__capacidad_maxima:
            raise GrupoLlenoError(
                f"El grupo {self.__codigo} alcanzó su capacidad máxima."
            )

        self.__estudiantes.append(estudiante)
        print(
            f"{estudiante.get_nombre()} se matriculó correctamente "
            f"en el grupo {self.__codigo}."
        )

    def retirar_estudiante(self, codigo_estudiantil):
        for estudiante in self.__estudiantes:
            if estudiante.get_codigo_estudiantil() == codigo_estudiantil:
                self.__estudiantes.remove(estudiante)
                print(
                    f"{estudiante.get_nombre()} se retiró correctamente "
                    f"del grupo {self.__codigo}."
                )
                return

        raise EstudianteNoMatriculadoError(
            f"El estudiante {codigo_estudiantil} no está matriculado "
            f"en el grupo {self.__codigo}."
        )

    def mostrar_estudiantes(self):
        print(f"=== ESTUDIANTES DEL GRUPO {self.__codigo} ===")

        if not self.__estudiantes:
            print("No hay estudiantes matriculados.")
            return

        for estudiante in self.__estudiantes:
            print(
                f"{estudiante.get_codigo_estudiantil()} - "
                f"{estudiante.get_nombre()}"
            )
            