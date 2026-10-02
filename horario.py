class Horario:
    """Representa el día, las horas y el salón de un grupo."""

    def __init__(self, dia, hora_inicio, hora_finalizacion, salon):
        self.__dia = dia
        self.__hora_inicio = hora_inicio
        self.__hora_finalizacion = hora_finalizacion
        self.__salon = salon

    def get_dia(self):
        return self.__dia

    def get_hora_inicio(self):
        return self.__hora_inicio

    def get_hora_finalizacion(self):
        return self.__hora_finalizacion

    def get_salon(self):
        return self.__salon

    def mostrar_informacion(self):
        print(f"Día: {self.__dia}")
        print(f"Hora de inicio: {self.__hora_inicio}")
        print(f"Hora de finalización: {self.__hora_finalizacion}")
        print(f"Salón: {self.__salon}")
        