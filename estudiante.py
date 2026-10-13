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
        promedio_acumulado
    ):
        super().__init__(identificacion, nombre, correo)
        self.__codigo_estudiantil = codigo_estudiantil
        self.__programa_academico = programa_academico
        self.__semestre = semestre
        self.__promedio_acumulado = promedio_acumulado

    def get_codigo_estudiantil(self):
        return self.__codigo_estudiantil

    def get_programa_academico(self):
        return self.__programa_academico

    def get_semestre(self):
        return self.__semestre

    def get_promedio_acumulado(self):
        return self.__promedio_acumulado

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Código estudiantil: {self.__codigo_estudiantil}")
        print(f"Programa: {self.__programa_academico.get_nombre()}")
        print(f"Semestre: {self.__semestre}")
        print(f"Promedio acumulado: {self.__promedio_acumulado}")

    def realizar_actividad_principal(self):
        print(
            f"El estudiante cursa "
            f"{self.__programa_academico.get_nombre()} "
            f"y se encuentra en el semestre {self.__semestre}."
        )