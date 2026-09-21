class Asignatura:
    def __init__(self, codigo, nombre, numero_creditos, programa_academico):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__numero_creditos = 1
        self.__programa_academico = programa_academico
        self.set_numero_creditos(numero_creditos)

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_numero_creditos(self):
        return self.__numero_creditos

    def get_programa_academico(self):
        return self.__programa_academico

    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self.__nombre = nombre
            print("Nombre de la asignatura actualizado correctamente.")
        else:
            print("Error: el nombre de la asignatura no puede estar vacío.")

    def set_numero_creditos(self, numero_creditos):
        if numero_creditos > 0:
            self.__numero_creditos = numero_creditos
            print("Número de créditos actualizado correctamente.")
        else:
            print("Error: el número de créditos debe ser mayor que cero.")

    def mostrar_informacion(self):
        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Número de créditos: {self.__numero_creditos}")
        print(
            f"Programa académico: "
            f"{self.__programa_academico.get_nombre()}"
        )
        