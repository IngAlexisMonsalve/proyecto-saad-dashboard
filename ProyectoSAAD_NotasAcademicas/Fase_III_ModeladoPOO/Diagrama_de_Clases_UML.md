# Fase III: Diagrama de Clases UML y Análisis POO

Este documento presenta el diseño de clases Orientado a Objetos para el sistema de Notas Académicas, incluyendo clases, atributos, métodos y relaciones.

---

## 1. Clases y sus Componentes

### Clase: Estudiante
*   **Atributos:**
    *   `idEstudiante: String`
    *   `nombre: String`
    *   `apellido: String`
    *   `email: String`
    *   `fechaNacimiento: Fecha`
    *   `carrera: String`
*   **Métodos:**
    *   `consultarNotas(): List<Calificacion>`
    *   `actualizarDatosPersonales(nuevosDatos): Boolean`

### Clase: Profesor
*   **Atributos:**
    *   `idProfesor: String`
    *   `nombre: String`
    *   `apellido: String`
    *   `email: String`
    *   `departamento: String`
*   **Métodos:**
    *   `asignarNota(calificacion): Boolean`
    *   `verListadoEstudiantes(curso): List<Estudiante>`

### Clase: Curso
*   **Atributos:**
    *   `idCurso: String`
    *   `nombre: String`
    *   `creditos: Integer`
    *   `codigo: String`
    *   `periodoAcademico: String`
*   **Métodos:**
    *   `obtenerEstudiantesInscritos(): List<Estudiante>`
    *   `obtenerCalificaciones(): List<Calificacion>`

### Clase: Calificacion
*   **Atributos:**
    *   `idCalificacion: String`
    *   `valor: Double`
    *   `tipo: String` (ej: 'Parcial', 'Final', 'Trabajo')
    *   `fecha: Fecha`
*   **Métodos:**
    *   `obtenerValor(): Double`
    *   `actualizarValor(nuevoValor): Boolean`

### Clase: Inscripcion
*   **Atributos:**
    *   `idInscripcion: String`
    *   `fechaInscripcion: Fecha`
    *   `estado: String` (ej: 'Activa', 'Retirada')
*   **Métodos:**
    *   `cambiarEstado(nuevoEstado): Boolean`

---

## 2. Relaciones entre Clases

*   **Estudiante --(1)-- tiene --(*)-- Inscripcion**
    *   Descripción: Un `Estudiante` puede tener múltiples `Inscripciones`. Cada `Inscripcion` pertenece a un único `Estudiante`.
    *   Tipo: Agregación (Inscripción puede existir sin Estudiante, aunque no tenga sentido en el contexto del sistema)

*   **Curso --(1)-- tiene --(*)-- Inscripcion**
    *   Descripción: Un `Curso` puede tener múltiples `Inscripciones`. Cada `Inscripcion` pertenece a un único `Curso`.
    *   Tipo: Agregación

*   **Profesor --(1)-- enseña --(*)-- Curso**
    *   Descripción: Un `Profesor` puede enseñar múltiples `Cursos`. Cada `Curso` es enseñado por un único `Profesor` (simplificado).
    *   Tipo: Asociación

*   **Inscripcion --(1)-- tiene --(*)-- Calificacion**
    *   Descripción: Una `Inscripcion` puede tener múltiples `Calificaciones`. Cada `Calificacion` está asociada a una única `Inscripcion`.
    *   Tipo: Composición (la Calificación no tiene sentido sin la Inscripción)

*   **Profesor --(1)-- asigna --(*)-- Calificacion**
    *   Descripción: Un `Profesor` asigna múltiples `Calificaciones`. Cada `Calificacion` es asignada por un único `Profesor`.
    *   Tipo: Asociación

---

## 3. Análisis Conceptual de Encapsulamiento y Herencia

*   **Encapsulamiento:** Todas las clases seguirán el principio de encapsulamiento, exponiendo solo la interfaz necesaria (métodos públicos) y manteniendo los atributos internos protegidos (privados). Por ejemplo, el `valor` de una `Calificacion` no debería ser modificado directamente, sino a través de un método `actualizarValor` que pueda incluir validaciones.
*   **Herencia:** En esta fase inicial, no se ha identificado una necesidad clara de herencia para las clases principales. Sin embargo, en una expansión futura, podríamos considerar clases base como `Persona` (para `Estudiante` y `Profesor`) o `EntidadAcademica` si se identifican atributos y métodos comunes que puedan ser reutilizados. Por ahora, se mantendrá un diseño plano.
