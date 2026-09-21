from persona import Persona


class Administrativo(Persona):
    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        numero_empleado,
        dependencia,
        cargo,
        jornada
    ):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = numero_empleado
        self.__dependencia = dependencia
        self.__cargo = cargo
        self.__jornada = jornada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de empleado: {self.__numero_empleado}")
        print(f"Dependencia: {self.__dependencia}")
        print(f"Cargo: {self.__cargo}")
        print(f"Jornada: {self.__jornada}")

    def realizar_actividad_principal(self):
        print(
            f"El administrativo se desempeña como "
            f"{self.__cargo} en la dependencia "
            f"{self.__dependencia}."
        )
        