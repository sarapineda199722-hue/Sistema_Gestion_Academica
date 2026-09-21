class Persona:
    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = ""
        self.set_correo(correo)

    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self.__nombre = nombre
            print("Nombre actualizado correctamente.")
        else:
            print("Error: el nombre no puede estar vacío.")

    def set_correo(self, correo):
        if correo.strip() != "":
            self.__correo = correo
            print("Correo actualizado correctamente.")
        else:
            print("Error: el correo electrónico no puede estar vacío.")

    def mostrar_informacion(self):
        print(f"Identificación: {self.__identificacion}")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo electrónico: {self.__correo}")
        