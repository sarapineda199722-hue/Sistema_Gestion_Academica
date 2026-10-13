class ProgramaAcademico:
    def __init__(self, codigo, nombre, facultad, numero_semestres):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__facultad = facultad
        self.__numero_semestres = numero_semestres

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_facultad(self):
        return self.__facultad

    def get_numero_semestres(self):
        return self.__numero_semestres

    def set_codigo(self, codigo):
        if codigo.strip() != "":
            self.__codigo = codigo
            print("Código actualizado correctamente.")
        else:
            print("Error: el código no puede estar vacío.")

    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self.__nombre = nombre
            print("Nombre del programa actualizado correctamente.")
        else:
            print("Error: el nombre del programa no puede estar vacío.")

    def set_facultad(self, facultad):
        if facultad.strip() != "":
            self.__facultad = facultad
            print("Facultad actualizada correctamente.")
        else:
            print("Error: la facultad no puede estar vacía.")

    def set_numero_semestres(self, numero_semestres):
        if numero_semestres > 0:
            self.__numero_semestres = numero_semestres
            print("Número de semestres actualizado correctamente.")
        else:
            print("Error: el número de semestres debe ser mayor que cero.")

    def mostrar_informacion(self):
        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Facultad: {self.__facultad}")
        print(f"Número de semestres: {self.__numero_semestres}")