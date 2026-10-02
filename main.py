from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo
from horario import Horario
from grupo_academico import GrupoAcademico
from catalogo_academico import CatalogoAcademico
from excepciones import (
    EstudianteYaMatriculadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError,
    AsignaturaNoEncontradaError,
    ProgramaNoEncontradoError
)


# Comprobar que Persona es abstracta.
print("=== PRUEBA DE PERSONA ABSTRACTA ===")

try:
    persona_ejemplo = Persona(
        "1001", "Sara Pineda", "sara@example.com"
    )
except TypeError:
    print("No se puede crear directamente una Persona.")

print("El programa continúa después de controlar el error.")


# Crear el programa académico.
programa_datos = ProgramaAcademico(
    "IAD",
    "Ingeniería Analítica de Datos",
    "Facultad de Ciencias e Ingenierías",
    9
)


# Crear asignaturas.
asignatura_programacion = Asignatura(
    "PROG1", "Programación I", 3, programa_datos
)

asignatura_estadistica = Asignatura(
    "EST1", "Estadística I", 3, programa_datos
)


# Registrar los objetos en el catálogo.
catalogo = CatalogoAcademico()
catalogo.agregar_programa(programa_datos)
catalogo.agregar_asignatura(asignatura_programacion)
catalogo.agregar_asignatura(asignatura_estadistica)


# Crear estudiantes.
estudiante_1 = Estudiante(
    "2001", "Sara Pineda", "sara@umanizales.edu.co",
    "E001", programa_datos, 2, 4.5
)

estudiante_2 = Estudiante(
    "2002", "Julián Loaiza", "julian@umanizales.edu.co",
    "E002", programa_datos, 3, 4.2
)

estudiante_3 = Estudiante(
    "2003", "María López", "maria@umanizales.edu.co",
    "E003", programa_datos, 2, 4.0
)


# Crear docentes.
docente_1 = Docente(
    "3001", "Laura Gómez", "laura@umanizales.edu.co",
    "D001", "Ciencias e Ingenierías", "Tiempo completo", 40
)

docente_2 = Docente(
    "3002", "Carlos Ramírez", "carlos@umanizales.edu.co",
    "D002", "Ciencias e Ingenierías", "Medio tiempo", 20
)


# Crear administrativos.
administrativo_1 = Administrativo(
    "4001", "Ana López", "ana@umanizales.edu.co",
    "A001", "Admisiones", "Coordinadora", "Diurna"
)

administrativo_2 = Administrativo(
    "4002", "Pedro Martínez", "pedro@umanizales.edu.co",
    "A002", "Biblioteca", "Auxiliar administrativo", "Nocturna"
)


# Mostrar el programa y las asignaturas.
print("\n=== INFORMACIÓN DEL PROGRAMA ===")
programa_datos.mostrar_informacion()

print("\n=== INFORMACIÓN DE LAS ASIGNATURAS ===")
asignatura_programacion.mostrar_informacion()
asignatura_estadistica.mostrar_informacion()


# Mantener las modificaciones y validaciones anteriores.
print("\n=== MODIFICACIONES VÁLIDAS ===")
estudiante_1.set_correo("sara.pineda@umanizales.edu.co")
programa_datos.set_numero_semestres(10)
asignatura_programacion.set_numero_creditos(4)

print("\n=== INFORMACIÓN ACTUALIZADA ===")
estudiante_1.mostrar_informacion()
programa_datos.mostrar_informacion()
asignatura_programacion.mostrar_informacion()

print("\n=== INTENTOS DE MODIFICACIÓN INVÁLIDA ===")
estudiante_1.set_correo("")
programa_datos.set_numero_semestres(0)
asignatura_programacion.set_numero_creditos(-3)


# Mantener el polimorfismo.
personas = [
    estudiante_1,
    estudiante_2,
    estudiante_3,
    docente_1,
    docente_2,
    administrativo_1,
    administrativo_2
]

print("\n=== RECORRIDO POLIMÓRFICO ===")

for persona in personas:
    print("\n--------------------------------")
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()


# Probar un horario.
print("\n=== PRUEBA DEL HORARIO ===")
horario_ejemplo = Horario("Lunes", "08:00", "10:00", "201")
horario_ejemplo.mostrar_informacion()


# Crear dos grupos con sus propios horarios.
grupo_1 = GrupoAcademico(
    "G01",
    asignatura_programacion,
    docente_1,
    2,
    "Lunes",
    "08:00",
    "10:00",
    "201"
)

grupo_2 = GrupoAcademico(
    "G02",
    asignatura_estadistica,
    docente_2,
    3,
    "Martes",
    "10:00",
    "12:00",
    "202"
)

print("\n=== INFORMACIÓN DE LOS GRUPOS ===")
grupo_1.mostrar_informacion_grupo()
print()
grupo_2.mostrar_informacion_grupo()


# Matrículas correctas.
print("\n=== MATRÍCULAS CORRECTAS ===")
grupo_1.matricular_estudiante(estudiante_1)
grupo_1.matricular_estudiante(estudiante_2)
grupo_2.matricular_estudiante(estudiante_3)

grupo_1.mostrar_estudiantes()
grupo_2.mostrar_estudiantes()


# Matrícula duplicada.
print("\n=== PRUEBA DE MATRÍCULA DUPLICADA ===")

try:
    grupo_1.matricular_estudiante(estudiante_1)
except EstudianteYaMatriculadoError as error:
    print(f"Error controlado: {error}")

print("El programa continúa después de la matrícula duplicada.")


# Grupo lleno.
print("\n=== PRUEBA DE GRUPO LLENO ===")

try:
    grupo_1.matricular_estudiante(estudiante_3)
except GrupoLlenoError as error:
    print(f"Error controlado: {error}")

print("El programa continúa después del intento de superar el cupo.")


# Retiro correcto.
print("\n=== RETIRO CORRECTO ===")
grupo_1.retirar_estudiante("E002")
grupo_1.mostrar_estudiantes()


# Retiro de un estudiante no matriculado.
print("\n=== PRUEBA DE RETIRO INEXISTENTE ===")

try:
    grupo_1.retirar_estudiante("E999")
except EstudianteNoMatriculadoError as error:
    print(f"Error controlado: {error}")

print("El programa continúa después del retiro inexistente.")


# Usar el cupo liberado.
print("\n=== MATRÍCULA EN EL CUPO LIBERADO ===")
grupo_1.matricular_estudiante(estudiante_3)
grupo_1.mostrar_estudiantes()


# Búsquedas correctas.
print("\n=== BÚSQUEDAS CORRECTAS ===")

programa_encontrado = catalogo.buscar_programa("IAD")
print(f"Programa encontrado: {programa_encontrado.get_nombre()}")

asignatura_encontrada = catalogo.buscar_asignatura("PROG1")
print(f"Asignatura encontrada: {asignatura_encontrada.get_nombre()}")


# Buscar una asignatura que no existe.
print("\n=== PRUEBA DE ASIGNATURA INEXISTENTE ===")

try:
    catalogo.buscar_asignatura("NO_EXISTE")
except AsignaturaNoEncontradaError as error:
    print(f"Error controlado: {error}")

print("El programa continúa después de la asignatura inexistente.")


# Buscar un programa que no existe.
print("\n=== PRUEBA DE PROGRAMA INEXISTENTE ===")

try:
    catalogo.buscar_programa("NO_EXISTE")
except ProgramaNoEncontradoError as error:
    print(f"Error controlado: {error}")

print("El programa continúa después del programa inexistente.")

print("\n=== FIN DE LAS PRUEBAS DE LA ACTIVIDAD 2 ===")
