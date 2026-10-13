# Sistema de Gestión Académica

## Integrante

- Sara Liliana Pineda Castro

## Descripción general

Este proyecto representa una primera versión de un sistema de gestión académica desarrollado en Python mediante programación orientada a objetos.

El sistema permite registrar y consultar información de personas, estudiantes, docentes, administrativos, programas académicos y asignaturas. También permite modificar algunos datos mediante validaciones.

## Funcionalidades

- Registrar personas.
- Crear programas académicos y asignaturas.
- Modificar datos de forma controlada.
- Validar correos electrónicos, semestres y créditos.
- Representar estudiantes, docentes y administrativos.
- Mostrar información diferente según el tipo de persona.
- Recorrer una colección de personas mediante polimorfismo.

## Estructura de los archivos

- `persona.py`: contiene la clase principal Persona.
- `programa_academico.py`: contiene la clase ProgramaAcademico.
- `asignatura.py`: contiene la clase Asignatura.
- `estudiante.py`: contiene la clase Estudiante.
- `docente.py`: contiene la clase Docente.
- `administrativo.py`: contiene la clase Administrativo.
- `main.py`: crea los objetos y ejecuta las pruebas del sistema.

## Conceptos aplicados

### Encapsulamiento

Los atributos están protegidos para evitar que se modifiquen directamente. Los cambios se realizan mediante métodos que validan la información ingresada.

Por ejemplo:

- El correo electrónico no puede estar vacío.
- El número de semestres debe ser mayor que cero.
- El número de créditos debe ser mayor que cero.

### Herencia

Las clases `Estudiante`, `Docente` y `Administrativo` heredan los datos y comportamientos generales de la clase `Persona`.

### Sobrescritura

Cada clase hija implementa su propia versión de los métodos `mostrar_informacion()` y `realizar_actividad_principal()`.

### Polimorfismo

Se crea una sola colección que contiene estudiantes, docentes y administrativos. Esta colección se recorre mediante un único ciclo, llamando los mismos métodos para todos los objetos. Python ejecuta automáticamente el comportamiento correspondiente a cada tipo de persona.

## Requisitos

- Python 3 instalado.
- Visual Studio Code o cualquier editor compatible con Python.

## Instrucciones para ejecutar el proyecto

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir la terminal.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

## Uso de inteligencia artificial

Se utilizó inteligencia artificial como apoyo para resolver dudas y revisar errores durante el desarrollo del proyecto.
