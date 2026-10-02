# Sistema de Gestión Académica

Proyecto de Programación I de la Universidad de Manizales.

La actividad 2 amplía el proyecto de la actividad 1 mediante una clase abstracta, grupos académicos, horarios, matrículas y manejo de excepciones.

## Requisitos y ejecución

Se necesita Python 3. No requiere instalar bibliotecas externas.

Para ejecutar el programa, abre la terminal en la carpeta del proyecto y escribe:

python main.py

El programa muestra pruebas en la consola. Los datos se mantienen en memoria durante la ejecución.

## Archivos del proyecto

| Archivo | Función |
|---------|---------|
| persona.py | Define la clase abstracta Persona. |
| estudiante.py | Define la clase Estudiante. |
| docente.py | Define la clase Docente. |
| administrativo.py | Define la clase Administrativo. |
| programa_academico.py | Define los programas académicos. |
| asignatura.py | Define las asignaturas y su programa académico. |
| horario.py | Define el día, las horas y el salón. |
| grupo_academico.py | Gestiona los grupos, sus matrículas y retiros. |
| excepciones.py | Define las excepciones propias del sistema. |
| catalogo_academico.py | Registra y busca programas y asignaturas. |
| main.py | Ejecuta las pruebas del proyecto. |

## Abstracción

Persona hereda de ABC y declara realizar_actividad_principal como método abstracto mediante @abstractmethod.

No se puede crear directamente una Persona. Se deben crear objetos de sus subclases: Estudiante, Docente o Administrativo.

Cada subclase implementa realizar_actividad_principal según su función dentro de la universidad.

En main.py se intenta crear una Persona y se captura el TypeError para demostrar esta restricción sin detener el programa.

## Relaciones entre objetos

Cada Asignatura está relacionada con un objeto ProgramaAcademico.

Cada GrupoAcademico recibe un objeto Asignatura y un objeto Docente. También mantiene una lista de objetos Estudiante.

El código estudiantil permite identificar a cada estudiante al matricularlo o retirarlo.

CatalogoAcademico almacena programas y asignaturas en diccionarios y permite buscarlos por su código.

## Composición entre GrupoAcademico y Horario

Cada GrupoAcademico crea su propio objeto Horario dentro de su constructor, utilizando el día, la hora de inicio, la hora de finalización y el salón recibidos.

Esta relación es composición porque el horario forma parte del grupo y es creado por él.

No se utiliza herencia entre estas clases: un grupo académico tiene un horario.

## Operaciones de los grupos

- mostrar_informacion_grupo: muestra la asignatura, el docente, el cupo, la cantidad de estudiantes y el horario.
- matricular_estudiante: agrega un estudiante después de verificar que no esté matriculado y que exista cupo.
- retirar_estudiante: elimina al estudiante identificado por su código.
- mostrar_estudiantes: muestra los códigos y nombres de los estudiantes matriculados.

## Excepciones personalizadas

Las excepciones se generan con raise en el método que detecta el problema y se capturan con try y except en main.py.

| Excepción | Situación |
|-----------|-----------|
| EstudianteYaMatriculadoError | El estudiante ya está matriculado en el grupo. |
| GrupoLlenoError | El grupo alcanzó su capacidad máxima. |
| EstudianteNoMatriculadoError | Se intenta retirar a un estudiante que no pertenece al grupo. |
| AsignaturaNoEncontradaError | No existe una asignatura con el código solicitado. |
| ProgramaNoEncontradoError | No existe un programa con el código solicitado. |

Después de capturar cada excepción, el programa muestra un mensaje comprensible y continúa con las demás pruebas.

## Polimorfismo

main.py reúne estudiantes, docentes y administrativos en una lista.

Durante el recorrido se ejecutan mostrar_informacion y realizar_actividad_principal sobre cada objeto.

Cada objeto utiliza la implementación correspondiente a su clase.

## Pruebas realizadas

1. Intento de crear directamente una Persona.
2. Presentación de programas y asignaturas.
3. Modificaciones válidas e inválidas de atributos.
4. Recorrido polimórfico de estudiantes, docentes y administrativos.
5. Presentación de un horario.
6. Creación y presentación de dos grupos académicos.
7. Matrículas correctas.
8. Intento de matrícula duplicada.
9. Intento de matrícula en un grupo lleno.
10. Retiro correcto de un estudiante.
11. Intento de retiro de un estudiante no matriculado.
12. Matrícula después de liberar un cupo.
13. Búsquedas correctas de programas y asignaturas.
14. Búsquedas de una asignatura y un programa inexistentes.

Los mensajes de error de estas pruebas son intencionales y permiten comprobar las validaciones.

## Alcance

El proyecto funciona en consola y almacena los datos en memoria. No incluye una base de datos ni una interfaz gráfica.

## Uso de inteligencia artificial

Se utilizó ChatGPT como apoyo para comprender los conceptos, elaborar código y revisar las pruebas.

Los integrantes deben revisar y comprender el código presentado y poder explicar su funcionamiento.
