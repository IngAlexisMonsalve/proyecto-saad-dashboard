# Fase I: DFD y Diccionario de Datos

Este documento contiene los entregables para la primera fase del proyecto SAAD: el Diagrama de Flujo de Datos (DFD) y el Diccionario de Datos.

---

## 1. Diagrama de Flujo de Datos (DFD) - Nivel 0 (Contexto)

Este diagrama muestra el sistema como un único proceso y su interacción con las entidades externas.

*   **Proceso Central:**
    *   `0.0 Sistema de Gestión Académica`
*   **Entidades Externas:**
    *   `Profesor`
    *   `Estudiante`
    *   `Control de Estudios`
*   **Flujos de Datos:**
    *   `Profesor` -> `Sistema`: `Notas y Asistencias`, `Información del Curso`
    *   `Sistema` -> `Profesor`: `Listado de Estudiantes`, `Reporte de Calificaciones (Parcial)`
    *   `Estudiante` -> `Sistema`: `Solicitud de Notas`, `Datos Personales (Actualización)`
    *   `Sistema` -> `Estudiante`: `Consulta de Notas`, `Historial Académico`
    *   `Control de Estudios` -> `Sistema`: `Registro de Cursos`, `Matrícula de Estudiantes`, `Políticas Académicas`
    *   `Sistema` -> `Control de Estudios`: `Reporte Consolidado de Notas`, `Estadísticas Académicas`

---

## 2. Diccionario de Datos (Versión Inicial)

A continuación se definen los flujos de datos identificados en el DFD de Nivel 0.

*   **Nombre del Flujo:** `Notas y Asistencias`
    *   **Descripción:** Calificaciones parciales, finales y registro de asistencia de los estudiantes para un curso específico.
    *   **Composición:** `ID_Curso + ID_Estudiante + Tipo_Nota (Parcial, Final) + Valor_Nota + Fecha + Estado_Asistencia`

*   **Nombre del Flujo:** `Información del Curso`
    *   **Descripción:** Datos generales y material de apoyo para un curso.
    *   **Composición:** `ID_Curso + Nombre_Curso + Contenido_Programatico + Fechas_Evaluaciones`

*   **Nombre del Flujo:** `Listado de Estudiantes`
    *   **Descripción:** Lista de todos los estudiantes inscritos en un curso.
    *   **Composición:** `{ID_Estudiante + Nombre_Estudiante + Email_Estudiante}` (se repite para cada estudiante)

*   **Nombre del Flujo:** `Solicitud de Notas`
    *   **Descripción:** Petición de un estudiante para ver sus calificaciones.
    *   **Composición:** `ID_Estudiante + ID_Curso (opcional)`

*   **Nombre del Flujo:** `Consulta de Notas`
    *   **Descripción:** Respuesta del sistema con las notas solicitadas por el estudiante.
    *   **Composición:** `ID_Curso + Nombre_Curso + Tipo_Nota + Valor_Nota`

*   **Nombre del Flujo:** `Registro de Cursos`
    *   **Descripción:** Datos para la creación o actualización de un curso en el sistema.
    *   **Composición:** `ID_Curso + Nombre_Curso + Creditos + Carrera_Asociada`

*   **Nombre del Flujo:** `Matrícula de Estudiantes`
    *   **Descripción:** Información sobre qué estudiantes están inscritos en qué cursos para un período académico.
    *   **Composición:** `{ID_Estudiante + ID_Curso}`

*   **Nombre del Flujo:** `Reporte Consolidado de Notas`
    *   **Descripción:** Informe final con las notas de todos los estudiantes en un período académico.
    *   **Composición:** `{ID_Estudiante + ID_Curso + Nota_Final}`

*(Nota: Otros flujos como `Datos Personales`, `Historial Académico`, etc., se definirán con una estructura similar a medida que se avance).*

---

## 3. Diagrama de Flujo de Datos (DFD) - Nivel 1

Este diagrama descompone el proceso `0.0 Sistema de Gestión Académica` en sus sub-procesos principales, mostrando la interacción con los almacenes de datos.

*   **Sub-procesos:**
    *   `1.0 Gestionar Cursos y Matrícula`
    *   `2.0 Gestionar Calificaciones`
    *   `3.0 Generar Reportes y Consultas`

*   **Almacenes de Datos:**
    *   `A1: ESTUDIANTES`
    *   `A2: CURSOS`
    *   `A3: MATRÍCULAS`
    *   `A4: CALIFICACIONES`

### Flujos Detallados por Proceso:

**Proceso 1.0: Gestionar Cursos y Matrícula**
*   **Entradas:**
    *   `Registro de Cursos` (desde `Control de Estudios`) -> Escribe en `A2: CURSOS`.
    *   `Matrícula de Estudiantes` (desde `Control de Estudios`) -> Escribe en `A3: MATRÍCULAS`.
    *   `Datos Personales (Actualización)` (desde `Estudiante`) -> Escribe en `A1: ESTUDIANTES`.
*   **Salidas/Accesos:**
    *   Lee/Verifica datos de `A1: ESTUDIANTES` y `A2: CURSOS` para validar la matrícula.

**Proceso 2.0: Gestionar Calificaciones**
*   **Entradas:**
    *   `Notas y Asistencias` (desde `Profesor`) -> Escribe en `A4: CALIFICACIONES`.
    *   `Información del Curso` (desde `Profesor`) -> Escribe en `A2: CURSOS`.
*   **Salidas/Accesos:**
    *   Lee de `A3: MATRÍCULAS` para verificar que el estudiante pertenece al curso.

**Proceso 3.0: Generar Reportes y Consultas**
*   **Entradas:**
    *   `Solicitud de Notas` (desde `Estudiante`).
*   **Salidas/Accesos:**
    *   `Consulta de Notas` -> para `Estudiante` (Lee de `A4`, `A2`).
    *   `Historial Académico` -> para `Estudiante` (Lee de `A4`, `A2`, `A1`).
    *   `Listado de Estudiantes` -> para `Profesor` (Lee de `A3`, `A1`).
    *   `Reporte de Calificaciones (Parcial)` -> para `Profesor` (Lee de `A4`, `A3`).
    *   `Reporte Consolidado de Notas` -> para `Control de Estudios` (Lee de `A4`, `A3`).
    *   `Estadísticas Académicas` -> para `Control de Estudios` (Lee y procesa datos de `A1`, `A2`, `A3`, `A4`).

