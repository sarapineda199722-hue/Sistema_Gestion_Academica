from persona import Persona


class Estudiante(Persona):
    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        codigo_estudiantil,
        programa_academico,
        semestre,
        promedio
    ):
        super().__init__(identificacion, nombre, correo)
        self.__codigo_estudiantil = codigo_estudiantil
        self.__programa_academico = programa_academico
        self.__semestre = semestre
        self.__promedio = promedio

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Código estudiantil: {self.__codigo_estudiantil}")
        print(
            f"Programa: {self.__programa_academico.get_nombre()}"
        )
        print(f"Semestre: {self.__semestre}")
        print(f"Promedio acumulado: {self.__promedio}")

    def realizar_actividad_principal(self):
        print(
            f"El estudiante cursa "
            f"{self.__programa_academico.get_nombre()} "
            f"y se encuentra en el semestre {self.__semestre}."
        )
        