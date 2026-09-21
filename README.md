# Sistema de Gestión Académica

Proyecto desarrollado en Python para representar un sistema de gestión académica mediante los principios de programación orientada a objetos.

## Integrantes

- Sara Liliana Pineda Castro
- Julián Loaiza Botero

## Objetivo

Desarrollar un programa que permita representar personas, estudiantes, docentes, administrativos, programas académicos y asignaturas, aplicando los conceptos de clases, objetos, encapsulamiento, herencia, sobrescritura de métodos y polimorfismo.

## Funcionalidades

- Creación de personas, programas académicos y asignaturas.
- Encapsulamiento de atributos.
- Validación del correo electrónico.
- Validación del número de semestres.
- Validación del número de créditos.
- Herencia desde la clase `Persona`.
- Clases `Estudiante`, `Docente` y `Administrativo`.
- Sobrescritura del método `mostrar_informacion()`.
- Implementación del método `realizar_actividad_principal()`.
- Recorrido polimórfico de una colección de personas.
- Pruebas de modificaciones válidas e inválidas.

## Estructura del proyecto

- `persona.py`: clase principal Persona.
- `programa_academico.py`: clase ProgramaAcademico.
- `asignatura.py`: clase Asignatura.
- `estudiante.py`: clase Estudiante.
- `docente.py`: clase Docente.
- `administrativo.py`: clase Administrativo.
- `main.py`: creación de objetos, validaciones y ejecución del programa.

## Requisitos

- Python 3.13 o una versión compatible.
- Visual Studio Code o cualquier editor compatible con Python.

## Ejecución

Para ejecutar el programa, se debe abrir una terminal dentro de la carpeta del proyecto y usar:

```bash
python main.py
