from persona import Persona


class Docente(Persona):
    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        numero_empleado,
        facultad,
        tipo_contratacion,
        horas_semanales
    ):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = numero_empleado
        self.__facultad = facultad
        self.__tipo_contratacion = tipo_contratacion
        self.__horas_semanales = horas_semanales

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de empleado: {self.__numero_empleado}")
        print(f"Facultad: {self.__facultad}")
        print(f"Tipo de contratación: {self.__tipo_contratacion}")
        print(f"Horas semanales: {self.__horas_semanales}")

    def realizar_actividad_principal(self):
        print(
            f"El docente orienta clases en la facultad "
            f"{self.__facultad}."
        )
        