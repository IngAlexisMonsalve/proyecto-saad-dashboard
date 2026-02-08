# Fase II: Diseño Lógico de la Función Crítica

Este documento contiene el pseudocódigo para la función más crítica del sistema, según lo definido en la Fase I.

*   **Función Crítica Seleccionada:** `Gestionar Calificaciones` (Proceso 2.0 del DFD Nivel 1).

---

## Pseudocódigo: Gestionar_Calificaciones

**Propósito:** Recibir los datos de una calificación enviados por un `Profesor`, validar que sean correctos y guardarlos en el almacén de datos correspondiente.

```plaintext
FUNCIÓN Gestionar_Calificaciones(datos_entrada):
  // Descripción: Procesa el flujo de datos "Notas y Asistencias".
  // Parámetros de entrada (datos_entrada): ID_Curso, ID_Estudiante, Tipo_Nota, Valor_Nota, Fecha, Estado_Asistencia.
  // Retorna: Mensaje de "Éxito" o "Error".

  // 1. Validación de Datos de Entrada
  // Se comprueba que los datos mínimos requeridos no estén vacíos.
  SI ID_Curso O ID_Estudiante O Valor_Nota SON NULOS O VACÍOS:
    RETORNAR "Error de Validación: Faltan datos obligatorios (Curso, Estudiante, Nota)."
  FIN SI

  // 2. Validación de Regla de Negocio
  // Se verifica que el estudiante esté realmente inscrito en el curso.
  matricula_es_valida = CONSULTAR en Almacén 'A3: MATRÍCULAS'
                           DONDE Estudiante = ID_Estudiante Y Curso = ID_Curso

  SI matricula_es_valida ES FALSO:
    RETORNAR "Error de Negocio: El estudiante no está inscrito en el curso especificado."
  FIN SI

  // 3. Proceso de Persistencia (Guardado)
  // Si todas las validaciones son exitosas, se guarda la información.
  // Se crea una estructura para la nueva calificación.
  nueva_calificacion = {
    id_curso: ID_Curso,
    id_estudiante: ID_Estudiante,
    tipo_de_nota: Tipo_Nota,
    valor_nota: Valor_Nota,
    fecha_de_registro: Fecha,
    asistencia: Estado_Asistencia
  }

  // Se envía la estructura al almacén de datos para ser guardada.
  GUARDAR nueva_calificacion en Almacén 'A4: CALIFICACIONES'

  // 4. Confirmación de Éxito
  // Se notifica que la operación fue exitosa.
  RETORNAR "Éxito: La calificación ha sido registrada correctamente."

FIN FUNCIÓN
```
