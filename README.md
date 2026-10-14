# Sistema de Gestión Académica

Proyecto de Programación I de la Universidad de Manizales.

## Integrante

- Sara Liliana Pineda Castro

## Descripción general

Este proyecto corresponde a la evolución del Sistema de Gestión Académica desarrollado en la Actividad 1.

La Actividad 2 incorpora una clase abstracta, grupos académicos, horarios, matrículas, retiros, búsquedas y excepciones personalizadas. El programa conserva la herencia, la sobrescritura y el polimorfismo implementados anteriormente.

## Requisitos para ejecutar el proyecto

- Python 3.
- Visual Studio Code o cualquier editor compatible con Python.
- No se necesitan bibliotecas externas.

## Instrucciones de ejecución

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir la terminal.
4. Ejecutar:

```bash
python main.py
```

## Estructura de los archivos

| Archivo | Descripción |
|---|---|
| `persona.py` | Define la clase abstracta Persona. |
| `estudiante.py` | Define la clase Estudiante. |
| `docente.py` | Define la clase Docente. |
| `administrativo.py` | Define la clase Administrativo. |
| `programa_academico.py` | Representa los programas académicos. |
| `asignatura.py` | Representa las asignaturas y su programa académico. |
| `horario.py` | Representa el día, las horas y el salón. |
| `grupo_academico.py` | Gestiona grupos, matrículas y retiros. |
| `excepciones.py` | Define las excepciones personalizadas. |
| `catalogo_academico.py` | Registra y busca programas y asignaturas. |
| `main.py` | Crea los objetos y ejecuta las pruebas del sistema. |

## Clase abstracta Persona

La clase `Persona` hereda de `ABC` y define `realizar_actividad_principal()` como método abstracto mediante `@abstractmethod`.

No se pueden crear directamente objetos de tipo `Persona`. Por eso se utilizan las clases especializadas `Estudiante`, `Docente` y `Administrativo`.

Cada clase derivada implementa `realizar_actividad_principal()` con un comportamiento diferente:

- El estudiante informa el programa que cursa y su semestre.
- El docente informa la facultad en la que orienta clases.
- El administrativo informa su cargo y dependencia.

## Relaciones entre las clases

Una `Asignatura` contiene una referencia a su `ProgramaAcademico`.

Un `GrupoAcademico` recibe objetos ya creados de `Asignatura` y `Docente`. También mantiene una colección de objetos `Estudiante` matriculados.

El `CatalogoAcademico` almacena programas y asignaturas y permite buscarlos mediante su código.

## Composición entre GrupoAcademico y Horario

Cada objeto `GrupoAcademico` crea y contiene su propio objeto `Horario`. El horario describe el día, la hora de inicio, la hora de finalización y el salón en los que se desarrolla el grupo.

Esta relación corresponde a composición porque el grupo **tiene un horario** como parte de su organización. No corresponde a herencia porque un grupo académico **no es un horario**.

## Operaciones de los grupos

La clase `GrupoAcademico` incluye los siguientes métodos:

- `mostrar_informacion_grupo()`: presenta los datos principales del grupo.
- `matricular_estudiante(estudiante)`: matricula un estudiante después de validar duplicados y capacidad.
- `retirar_estudiante(codigo_estudiantil)`: retira un estudiante mediante su código.
- `mostrar_estudiantes()`: muestra los estudiantes matriculados.

## Excepciones personalizadas

| Excepción | Situación controlada |
|---|---|
| `EstudianteYaMatriculadoError` | El estudiante ya pertenece al grupo. |
| `GrupoLlenoError` | El grupo alcanzó su capacidad máxima. |
| `EstudianteNoMatriculadoError` | Se intenta retirar a un estudiante que no pertenece al grupo. |
| `AsignaturaNoEncontradaError` | No existe una asignatura con el código solicitado. |
| `ProgramaNoEncontradoError` | No existe un programa con el código solicitado. |

Las excepciones se lanzan con `raise` desde el método que detecta el problema y se capturan en `main.py` mediante bloques `try` y `except`. Después de mostrar un mensaje comprensible, el programa continúa su ejecución.

## Polimorfismo

Los estudiantes, docentes y administrativos se almacenan en una misma colección. La colección se recorre mediante un único ciclo que llama a `mostrar_informacion()` y `realizar_actividad_principal()`.

Cada objeto ejecuta automáticamente la implementación correspondiente a su clase, sin utilizar condicionales para identificar su tipo.

## Pruebas realizadas

El archivo `main.py` demuestra:

1. Que no se puede crear directamente una persona.
2. La creación de programas, asignaturas, estudiantes, docentes y horarios.
3. La creación de dos grupos académicos.
4. Matrículas correctas.
5. El intento de matrícula duplicada.
6. El intento de superar la capacidad de un grupo.
7. El retiro correcto de un estudiante.
8. El intento de retirar un estudiante no matriculado.
9. La búsqueda de una asignatura inexistente.
10. La búsqueda de un programa inexistente.
11. La continuidad del programa después de cada excepción.
12. El recorrido polimórfico de las personas vinculadas.

## Uso de inteligencia artificial

Se utilizó inteligencia artificial como apoyo para resolver dudas y revisar errores.