from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo


# Comprobar que Persona es una clase abstracta.
print("=== PRUEBA DE PERSONA ABSTRACTA ===")

try:
    persona_ejemplo = Persona(
        "1001",
        "Sara Pineda",
        "sara@example.com"
    )
except TypeError:
    print("No se puede crear directamente una Persona.")
    print("Se debe crear un Estudiante, Docente o Administrativo.")

print("El programa continúa después de controlar el error.")


# Crear el programa y la asignatura.
programa_datos = ProgramaAcademico(
    "IAD",
    "Ingeniería Analítica de Datos",
    "Facultad de Ciencias e Ingenierías",
    9
)

asignatura_programacion = Asignatura(
    "PROG1",
    "Programación I",
    3,
    programa_datos
)


# Crear estudiantes.
estudiante_1 = Estudiante(
    "2001",
    "Sara Pineda",
    "sara@umanizales.edu.co",
    "E001",
    programa_datos,
    2,
    4.5
)

estudiante_2 = Estudiante(
    "2002",
    "Julián Loaiza",
    "julian@umanizales.edu.co",
    "E002",
    programa_datos,
    3,
    4.2
)


# Crear docentes.
docente_1 = Docente(
    "3001",
    "Laura Gómez",
    "laura@umanizales.edu.co",
    "D001",
    "Ciencias e Ingenierías",
    "Tiempo completo",
    40
)

docente_2 = Docente(
    "3002",
    "Carlos Ramírez",
    "carlos@umanizales.edu.co",
    "D002",
    "Ciencias e Ingenierías",
    "Medio tiempo",
    20
)


# Crear administrativos.
administrativo_1 = Administrativo(
    "4001",
    "Ana López",
    "ana@umanizales.edu.co",
    "A001",
    "Admisiones",
    "Coordinadora",
    "Diurna"
)

administrativo_2 = Administrativo(
    "4002",
    "Pedro Martínez",
    "pedro@umanizales.edu.co",
    "A002",
    "Biblioteca",
    "Auxiliar administrativo",
    "Nocturna"
)


# Mostrar el programa y la asignatura.
print("\n=== INFORMACIÓN DEL PROGRAMA ===")
programa_datos.mostrar_informacion()

print("\n=== INFORMACIÓN DE LA ASIGNATURA ===")
asignatura_programacion.mostrar_informacion()


# Conservar la demostración de modificaciones y validaciones.
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


# Mantener el polimorfismo de la actividad 1.
personas = [
    estudiante_1,
    estudiante_2,
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

print("\n=== FIN DE LA PRUEBA DE LA FASE 1 ===")
